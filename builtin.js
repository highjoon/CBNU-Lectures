const os = require('os');
const path = require('path');

// console.log(os.arch());
// // console.log(os.cpus());
// console.log(os.freemem());
// console.log(os.totalmem());

console.log(path.sep);
console.log(__filename);
console.log(path.dirname(__filename));
console.log(path.extname(__filename));
console.log(path.basename(__filename, '.js'));