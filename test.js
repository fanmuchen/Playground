function replaceSpace(str) {
    var result = "";
    for (var i = 0; i < str.length; i++) {
        if (str[i] == "\n") {
            result += " ";
        } else {
            result += str[i];
        }
    }
    return result;
}

var str = "hello\nworld";
console.log(replaceSpace(str));