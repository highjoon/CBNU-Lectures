const express = require('express');
const morgan = require('morgan');
const path = require('path');
const nunjucks = require('nunjucks');
const createError = require('http-errors');
const pageRouter = require('./routes/page.router');

const app = express();            // Express Application 객체 생성

// res.render() 함수로 views 디렉터리 내의 html을 nunjucks 엔진으로 렌더링하도록 설정
nunjucks.configure('views', {
    express: app,
    watch: true
});

// (렌더링 파일의 확장자가 html 파일이 되도록) view engine 설정
app.set('view engine', 'html');

app.use(morgan('dev'));     // morgan('dev')가 미들웨어 함수를 리턴
app.use('/public', express.static(path.join(__dirname, 'public')));

app.use('/', pageRouter);

app.use((req,res,next)=>{
    next(createError(404));
});

app.use((err,req,res,next)=>{
    res.locals.message = err.message;
    res.locals.status = err.status;
    res.render('error');
});

app.listen(3000, () => console.log('Server Running on 3000!'));