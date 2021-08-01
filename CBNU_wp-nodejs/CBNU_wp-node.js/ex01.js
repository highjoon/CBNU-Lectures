const say = require('./module1');
const module2 = require('./module2');

say('길동');
module2.printMessage('DEBUG', '메시지 테스트');
console.log(module2.date);
module2.printDate();