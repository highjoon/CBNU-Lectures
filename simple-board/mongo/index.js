const mongoose = require('mongoose');
const { MONGO_URL } = require('../env');

function connect() {
  return mongoose.connect(MONGO_URL, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
    useCreateIndex: true,
    useFindAndModify: true,
  });
}

const { connection } = mongoose;

connection.on('error', err => console.error('MongoDB 연결 에러'));
connection.on('open', () => console.log('MongoDB 연결 성공'));
connection.on('disconnected', () => {
    console.error('MongoDB와의 연결이 끊겼습니다. 연결을 재시도합니다.');
    connect();
  });
  
  const models = {};
  
  // 여기에 모델들을 추가해 나감
  models.User = require('./user.model');
  
  
  module.exports = { connect, mongoose, models };
  