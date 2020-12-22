const { Op } = require('sequelize');
const schedule = require('node-schedule');

const { Good, Auction, User, sequelize } = require('./models');

// 24시간 전에 생성되었는데 낙찰되지 못한 상품들 (에러)
module.exports = async () => {
  console.log('checkAuction');
  try {
    const yesterday = new Date();
    yesterday.setDate(yesterday.getDate() - 1); // 어제 시간
    const targets = await Good.findAll({
      where: {
        SoldId: null,
        createdAt: { [Op.lte]: yesterday },
      },
    });

    // 찾은 후 낙찰시키는 과정
    targets.forEach(async (target) => {
      const success = await Auction.findOne({
        where: { GoodId: target.id },
        order: [['bid', 'DESC']],
      });
      await Good.update({ SoldId: success.UserId }, { where: { id: target.id } });
      await User.update({
        money: sequelize.literal(`money - ${success.bid}`),
      }, {
        where: { id: success.UserId },
      });
    });
    const unsold = await Good.findAll({
      where: {
        SoldId: null,
        createdAt: { [Op.gt]: yesterday },
      },
    });

    // 경매가 시작한 후 24시간이 아직 지나지 않은 상품들은 스케쥴링
    unsold.forEach((target) => {
      const end = new Date(unsold.createdAt);
      end.setDate(end.getDate() + 1);
      schedule.scheduleJob(end, async () => {
        const success = await Auction.findOne({
          where: { GoodId: target.id },
          order: [['bid', 'DESC']],
        });
        await Good.update({ SoldId: success.userId }, { where: { id: target.id } });
        await User.update({
          money: sequelize.literal(`money - ${success.bid}`),
        }, {
          where: { id: success.UserId },
        });
      });
    });
  } catch (error) {
    console.error(error);
  }
};
