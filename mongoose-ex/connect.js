const mongoose = require('mongoose');

const MONGO_URL = 'mongodb://localhost/mongoose-db';    // 데이터베이스 명은 mongoose-db

mongoose.connect(MONGO_URL, {
    useNewUrlParser: true,
    useUnifiedTopology: true
});

mongoose.connection.on('error', err => console.error('MongoDB 연결 에러'));
mongoose.connection.on('on', () => console.error('MongoDB 연결 성공'));
mongoose.connection.on('disconnected', () => {
    console.error('MongoDB와의 연결이 끊겼습니다. 연결을 재시도합니다.');
    mongoose.connect(MONGO_URL);
});