import express, { static, json, urlencoded } from 'express';
const PORT = process.env.PORT;
import { join } from 'path';
import morgan from 'morgan';
import cookieParser from 'cookie-parser';
import session from 'express-session';
import { initialize, session as _session } from 'passport';
import { configure } from 'nunjucks';
import { config } from 'dotenv';

config();
import indexRouter from './routes/index';
import authRouter from './routes/auth';
import { sequelize } from './models';
import passportConfig from './passport';
import webSocket from './socket';
import sse from './sse';
import checkAuction from './checkAuction';

const app = express();
passportConfig();

// 서버를 재부팅하더라도 경매 항목이 유지되도록 checkAuction 모듈을 통해 설정
checkAuction();

app.set('port', process.env.PORT || 3050);
app.set('view engine', 'html');
configure('views', {
    express: app,
    watch: true
});
sequelize.sync({force: false}).then(() => {
    console.log('데이터베이스 연결 성공');
}).catch((err) => {
    console.error(err);
});

const sessionMiddleware = session({
    resave: false,
    saveUninitialized: false,
    secret: process.env.COOKIE_SECRET,
    cookie: {
        httpOnly: true,
        secure: false
    }
});

app.use(morgan('dev'));
app.use(static(join(__dirname, 'public')));
app.use('/img', static(join(__dirname, 'uploads')));
app.use(json());
app.use(urlencoded({extended: false}));
app.use(cookieParser(process.env.COOKIE_SECRET));
app.use(sessionMiddleware);
app.use(initialize());
app.use(_session());

app.use('/', indexRouter);
app.use('/auth', authRouter);

app.use((req, res, next) => {
    const error = new Error(`${
        req.method
    } ${
        req.url
    } 라우터가 없습니다.`);
    error.status = 404;
    next(error);
});

app.use((err, req, res, next) => {
    res.locals.message = err.message;
    res.locals.error = process.env.NODE_ENV !== 'production' ? err : {};
    res.status(err.status || 500);
    res.render('error');
});

const server = app.listen(app.get('port'), () => {
    console.log(app.get('port'), '번 포트에서 대기중');
});

// http 서버에 웹소켓, ServerSentEvent 연결
webSocket(server, app);
sse(server);
