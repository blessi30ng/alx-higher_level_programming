#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
	let lol = 0;
	for (const i in list) {
		if (list[i] == searchElement) {
			lol++;
		}
	}
	return lol;
};
