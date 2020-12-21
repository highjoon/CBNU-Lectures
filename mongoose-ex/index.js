const input = require('./utils/input');
const { connect, models: { User } } = require('./models');

async function run() {
  let username;

  await connect(); // MongoDB에 연결될 때까지 기다림

  while((username = await input('username(exit 입력시 종료): ') !== 'exit')) {
    const user = { username };
    user.password = await input('password: ');
    user.email = await input('email: ');

    try {
      const userInstance = await User.create(user);
      console.log(`${userInstance.username}을 DB에 저장`);
    } catch (err) {
      console.error(err);
    }
  }

  try {
    const users = await User.find();
    users.forEach(user => console.log(user));
  } catch (err) {
    console.error(err);
  }
  process.exit();
}

run();
