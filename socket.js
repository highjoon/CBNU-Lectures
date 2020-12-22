const SocketIO = require('socket.io');

module.exports = (server, app) => {
  const io = SocketIO(server, { path: '/socket.io' });
  app.set('io', io);
  io.on('connection', (socket) => { // 웹 소켓 연결 시
    const req = socket.request;
    const { headers: { referer } } = req;
    const roomId = referer.split('/')[referer.split('/').length - 1];
    // 경매방에 참가하는 소켓
    socket.join(roomId);
    // 경매방에서 퇴장했을 때의 소켓
    // roomId = Good 테이블의 Raw id
    socket.on('disconnect', () => {
      socket.leave(roomId);
    });
  });
};
