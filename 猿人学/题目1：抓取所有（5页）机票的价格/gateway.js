var window_atob = require("./window_atob")


function getM() {

    var timestamp = Date["parse"](new Date()) + (16798545 + -72936737 + 156138192)
    var data = window_atob["f"](timestamp.toString());

    return data + "丨" + timestamp / (-1 * 3483 + -9059 + 13542);

}

module.exports = {
    getM: getM
};


