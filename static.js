const express = require('express');
const morgan = require('morgan');
const path = require('path');

const app = express();            // Express Application 객체 생성

app.use(morgan('dev'));     // morgan('dev')가 미들웨어 함수를 리턴
app.use('/public', express.static(path.join(__dirname, 'public')));

app.get('/', (req, res) => {
    res.send('<h1>Hello Express</h1>');
});

app.get('/another', (req, res) => {
    res.send('<h1>Another Page!</h1>');
});

app.listen(3000, () => console.log('Server Running on 3000!'));