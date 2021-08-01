const express = require('express');
const morgan = require('morgan');
const createError = require('http-errors');
const nunjucks = require('nunjucks');
const { join } = require('path');
const cookieParser = require('cookie-parser');
const session = require('express-session');
const { IS_DEV, COOKIE_SECRET } = require('./env');
const { connect, mongoose } = require('./mongo');
const MongoStore = require('connect-mongo')(session);
const flash = require('connect-flash');
const { authenticated } = require('./middlewares/auth');
const pageRouter = require('./routes/page.router');
const authRouter = require('./routes/auth.router');

const app = express();

nunjucks.configure('views', {
  express: app,
  watch: true,
});
app.set('view engine', 'html');

app.use(morgan(IS_DEV ? 'dev' : 'combined'));
app.use('/public', express.static(join(__dirname, 'public')));
// 요청 메시지의 본문(폼 데이터)을 파싱하기 위한 미들웨어 추가
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(cookieParser(COOKIE_SECRET));
app.use(session({
  resave: false,
  saveUninitialized: false,
  secret: COOKIE_SECRET,
  cookie: {
    httpOnly: true,
    secure: false,
  },
  store: new MongoStore({ mongooseConnection: mongoose.connection })
}));
app.use(flash());
app.use(authenticated);  // 로그인한 경우 locals 영역에 로그인 정보를 저장하고 다음 미들웨어로 넘어 감

app.use(pageRouter);
app.use(authRouter); // 회원가입 및 로그인 관련 처리를 위한 라우터 추가

app.use((req, res, next) => {
  next(createError(404));
});
app.use((err, req, res, next) => {
  res.locals.message = err.message;
  res.locals.status = err.status;
  res.render('error', { title: 'Simple Board - Error' });
});

module.exports = app;
