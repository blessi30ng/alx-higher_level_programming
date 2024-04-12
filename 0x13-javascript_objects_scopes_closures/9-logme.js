#!/usr/bin/node
let lol = 0;
exports.logMe = function (item) {
	console.log(lol + ': ' + item);
	lol++;
};
