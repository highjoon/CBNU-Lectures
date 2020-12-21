const http = require('http');
const fs = require('fs');       // 파일시스템 (fs) 모듈 로드. 파일을 읽어올 수 있음.

const server = http.createServer((req, res) => {
    fs.readFile("./index.html", (err, data) => {
        if (err) throw err;
        res.end(data);
    });
});

server.listen(8080, () => {
    // listen 메소드를 호출하면 서버는 요청을 기다림
    console.log('8080번 포트에서 서버 실행 중...');
});

server.on('error', err => console.error(err));