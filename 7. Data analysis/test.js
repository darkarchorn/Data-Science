var arr = ["","1","1","","2"]
var error_yn = "N"
var a = ""

function isValid(arr) {
    let prev = null;
    for (let item of arr) {
      if (item === "") continue; // skip empty strings
      if (prev !== null && item !== prev) return false; // if different, invalid
      prev = item;
    }
    return true;
  }