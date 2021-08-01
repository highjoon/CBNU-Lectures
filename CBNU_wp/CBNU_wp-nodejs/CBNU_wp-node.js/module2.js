const date = new Date();
function printMsg(tag, msg) {
    console.log(`${tag}:::${msg}`);
}

function printDate() {
    console.log(date);
}

exports.date = date;
exports.printMessage = printMsg;
exports.printDate = printDate;


// module.exports = {
//     date,
//     printMessage: printMsg,
//     printDate
// };