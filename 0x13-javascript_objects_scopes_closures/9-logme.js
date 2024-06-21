#!i/usr/bin/node

let nag = 0;

exports.logMe = function (item) {
  console.log(nag + ': ' + item);
  nag++;
};
