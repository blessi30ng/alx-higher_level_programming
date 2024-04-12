#!/usr/bin/node
exports.esrever = function (list) {
	const rever = [];
	for (let i = 0; i < list.length; i++) {
		rever[list.length - i - 1] = list[i];
	}
	return rever;
};
