const say = require('./module1');
const { printMessage, date, printDate } = require('./module2');

say('길동');
printMessage('DEBUG', '메시지 테스트');
console.log(date)
printDate();