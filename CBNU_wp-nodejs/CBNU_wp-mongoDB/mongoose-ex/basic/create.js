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

// 스키마 정의
const userSchema = new mongoose.Schema({
    username: {
        type: String,       // username 필드의 값은 문자열 타입
        unique: true,       // unique 인덱스 생성 (Collection에 username 값이 중복된 문서가 생성될 수 없음)
        required: true,     // mongoose validator: username은 반드시 필요한 필드
    },
    password: String,       // password 필드의 값은 문자열 타입
    email: String,          // email 필드의 값은 문자열 타입
    joinedAt: {
        type: Date,         // joinedAt 필드의 값은 Date 타입
        default: Date.now   // 값이 입력되지 않을 경우 기본값은 문서가 생성되는 시점의 시간
    }
});

// User 모델 생성 (실제 MongoDB에는 users Collection이 생성)
const User = mongoose.model('User', userSchema);

const user1 = {username:'hong', password:'asdf', email:'hong@example.com'};
const user2 = {username:'lim', password:'1234', email:'lim@exmpale.com'};

// 방법 1
const user1Instance = new User(user1);

user1Instance.save()
.then(()=>console.log(`${user1Instance.username}을 DB에 저장`))
.catch(err=>console.error(err));

// 방법 2
User.create(user2)
.then(instance=>console.log(`${instance.username}을 DB에 저장`))
.catch(console.error);