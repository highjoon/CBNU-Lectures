const mongoose = require('mongoose');

const schema = new mongoose.Schema({
  username: {
    type: String,
    unique: true,
    required: true,
  },
  password: String,
  email: String
}, {
  // Schema 생성시 두번째 인자는 옵션이며,
  // timestamps 옵션의 createdAt은 문서 생성 시 자동으로 생성 시간을 저장할 필드 지정
  // timestamps 옵션의 updatedAt은 문서 갱신 시 자동으로 갱신한 시간을 저장할 필드 지정
  // false 값을 주면 생성하지 않음
  // true를 주면 createdAt은 'createdAt'으로 updatedAt은 'updatedAt'으로 필드 지정
  timestamps: { createdAt: 'joinedAt', updatedAt: false }
});


// 외부 모듈에서 User 모델을 사용할 수 있도록 export 한다.
module.exports = mongoose.model('User', userSchema);
