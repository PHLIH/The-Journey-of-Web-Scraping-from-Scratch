
const encrypt = require("./window_b")

const date =  Date["parse"](new Date()) + (16798545 + -72936737 + 156138192)
const _0x57feae = encrypt["hex_md5"](date.toString());


const m = _0x57feae + '|' + date / (-1 * 3483 + -9059 + 13542)

console.log(date)
console.log(m)






