const express = require('express');
const morgan = require('morgan');

const app = express();  // express application 객체 생성

app.set('Hello', 'Hello User');

app.use(morgan('combined'));

// 루트 경로(/)로 GET 요청이 왔을 경우 응답
app.get('/', (req, res) => {
    console.log(app.get('Hello'));
    res.send('<h1>Hello Express</h1>');
});

// another 경로로 GET 요청이 왔을 경우 응답
app.get('/another', (req, res) => {
    res.send('<h1>Another Page</h1>');
});

app.listen(3000, () => console.log('Server Running on 3000!'));