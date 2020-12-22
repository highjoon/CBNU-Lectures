const express = require('express');
const multer = require('multer');
const path = require('path');
const fs = require('fs');
const schedule = require('node-schedule');

const { Good, Auction, User, sequelize } = require('../models');
const { isLoggedIn, isNotLoggedIn } = require('./middlewares');

const router = express.Router();

// 로그인 했을 때 user에 회원정보 입력하는 라우터
router.use((req, res, next) => {
  res.locals.user = req.user;
  next();
});

// 경매가 진행 중인 상품 모두를 화면에 렌더링하는 라우터
// SoldId: null => 낙찰되지 않은 상품들만 표시
router.get('/', async (req, res, next) => {
  try {
    const goods = await Good.findAll({ where: { SoldId: null } });
    res.render('main', {
      title: 'Auction',
      goods,
    });
  } catch (error) {
    console.error(error);
    next(error);
  }
});

// 회원가입 페이지 라우터
router.get('/join', isNotLoggedIn, (req, res) => {
  res.render('join', {
    title: '회원가입 - Auction',
  });
});

// 상품 등록 라우터
router.get('/good', isLoggedIn, (req, res) => {
  res.render('good', { title: '상품 등록 - Auction' });
});

// 상품 업로드 라우터.
try {
  fs.readdirSync('uploads');
} catch (error) {
  console.error('uploads 폴더가 없어 uploads 폴더를 생성합니다.');
  fs.mkdirSync('uploads');
}

// 상품 이미지 업로드를 위해 multer 사용
const upload = multer({
  storage: multer.diskStorage({
    destination(req, file, cb) {
      cb(null, 'uploads/');
    },
    filename(req, file, cb) {
      const ext = path.extname(file.originalname);
      cb(null, path.basename(file.originalname, ext) + new Date().valueOf() + ext);
    },
  }),
  // 파일 크기 제한.
  limits: { fileSize: 5 * 1024 * 1024 },
});

// 상품을 등록한 사람의 정보 라우터.
router.post('/good', isLoggedIn, upload.single('img'), async (req, res, next) => {
  try {
    const { name, price } = req.body;
    const good = await Good.create({
      OwnerId: req.user.id,
      name,
      img: req.file.filename,
      price,
    });
    const end = new Date();
    end.setDate(end.getDate() + 1); // 1시간 뒤
    // 1시간 뒤에 함수 호출
    schedule.scheduleJob(end, async () => {
      // 절차 중 일부는 진행되고, 일부는 오류로 진행되지 않는 불상사를 방지하기 위해 SQL 중 where에 transaction 설정
      const t = await sequelize.transaction();
      try {
        // 상품 경매 내역 출력
        const success = await Auction.findOne({
          // 입찰가격을 내림차순한 다음 findOne으로 가장 높은 입찰가를 저장
          where: { GoodId: good.id },
          order: [['bid', 'DESC']],
          transaction: t
        });
        // 낙찰자 Id에는 입찰자 Id 입력
        await Good.update({ SoldId: success.UserId }, { where: { id: good.id }, transaction: t });
        // 사용자 잔액에서 낙찰한 금액만큼 차감 (sequelize.literal)
        await User.update({
          money: sequelize.literal(`money - ${success.bid}`),
        }, {
          where: { id: success.UserId },
          transaction: t
        });
        await t.commit();
      } catch (error) {
        await t.rollback();
      }
    });
    res.redirect('/');
  } catch (error) {
    console.error(error);
    next(error);
  }
});

// 로그인이 되어있어야 하며, 입찰 화면으로 이동하는 라우터
router.get('/good/:id', isLoggedIn, async (req, res, next) => {
  try {
    // Promise.all을 통해 good, auction 변수에 각각 저장
    const [good, auction] = await Promise.all([
      // 경매 상품 (findOne)
      Good.findOne({
        where: { id: req.params.id },
        include: {
          model: User,
          as: 'Owner',
        },
      }),
      // 경매 상품에 대한 입찰 내역 (findAll)
      Auction.findAll({
        where: { GoodId: req.params.id },
        include: { model: User },
        // 경매가격, 오름차순
        order: [['bid', 'ASC']],
      }),
    ]);
    res.render('auction', {
      title: `${good.name} - Auction`,
      good,
      auction,
    });
  } catch (error) {
    console.error(error);
    next(error);
  }
});

// 상품이 존재하는지 체크하는 라우터
router.post('/good/:id/bid', isLoggedIn, async (req, res, next) => {
  try {
    const { bid, msg } = req.body;
    const good = await Good.findOne({
      where: { id: req.params.id },
      include: { model: Auction },
      order: [[{ model: Auction }, 'bid', 'DESC']],
    });
    // 시작 가격보다 입찰가가 높아야한다는 제한
    if (good.price >= bid) {
      return res.status(403).send('시작 가격보다 높게 입찰해야 합니다.');
    }

    // 경매 종료 여부 확인 (24시간이 지났는지? 24간 안에 입찰되었는지?)
    // 경매는 24시간 동안 진행되도록 설정 (1000 * 60 * 60 * 24)
    if (new Date(good.createdAt).valueOf() + (1000 * 60 * 60 * 24) < new Date()) {
      return res.status(403).send('경매가 이미 종료되었습니다');
    }

    // 직전의 입찰보다 더 높은 입찰가를 제시해야한다는 제한
    if (good.Auctions[0] && good.Auctions[0].bid >= bid) {
      return res.status(403).send('이전 입찰가보다 높아야 합니다');
    }

    // 모든 입찰 과정을 마친 후의 경매 내역 저장
    const result = await Auction.create({
      bid,
      msg,
      UserId: req.user.id,
      GoodId: req.params.id,
    });

    // 실시간으로 입찰 내역을 전송
    // 가격, 메시지, 입찰자 닉네임
    req.app.get('io').to(req.params.id).emit('bid', {
      bid: result.bid,
      msg: result.msg,
      nick: req.user.nick,
    });
    return res.send('ok');
  } catch (error) {
    console.error(error);
    return next(error);
  }
});

router.get('/list', isLoggedIn, async (req, res, next) => {
  try {
    const goods = await Good.findAll({
      // 사용자가 낙찰 받은 상품 표시
      where: { SoldId: req.user.id },
      include: { model: Auction },
      order: [[{ model: Auction }, 'bid', 'DESC']],
    });
    res.render('list', { title: '낙찰 목록 - Auction', goods });
  } catch (error) {
    console.error(error);
    next(error);
  }
});

module.exports = router;
