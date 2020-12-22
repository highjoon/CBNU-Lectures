const SSE = require('sse');

// Express 서버와 연결
module.exports = (server) => {
  const sse = new SSE(server);
  sse.on('connection', (client) => { // ServerSent이벤트 연결
    // Client에게 서버 시간을 보여줌
    setInterval(() => {
        // 숫자를 문자로 전환
      client.send(Date.now().toString());
    }, 1000);
  });
};
