const http = require('http'); // http 모듈 로드

const server = http.createServer((req, res) => {
    // 요청(req)에 대해서 어떻게 응답(res)할지 작성
    // end로 끝냄.

    console.log(req.url);
    console.log(req.method);
    if (req.url == '/user') {
        res.end('<h1>User Page!</h1>');
    } else if (req.url == '/') {
        res.write("<h1>Index Page!</h1>");
    } else {
        res.end('<h1>Not Found!</h1>');
    }
});

server.listen(8080, () => {
    //listen 메소드를 호출하면 서버는 요청을 기다림
    console.log('8080번 포트에서 서버 실행 중...');
});

server.on('error', err => console.error(err));
// addEventListener과 같은 기능이라고 볼 수 있음.