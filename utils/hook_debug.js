

// 过debugger—1 constructor 构造器构造出来的
var _constructor = constructor;
Function.prototype.constructor = function(s) {
    if (s == "debugger") {
        console.log(s);
        return null;
    }
    return _constructor(s);
}

// 过debugger—2 eval的
(function() {
    'use strict';
    var eval_ = window.eval;
    window.eval = function(x) {
        eval_(x.replace("debugger;", "  ; "));
    }
    ;
    window.eval.toString = eval_.toString;
}
)();









