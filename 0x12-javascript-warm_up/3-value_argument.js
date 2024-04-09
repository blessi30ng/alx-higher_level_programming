#!/usr/bin/node
const lol = process.argv;
if (lol[2] === undefined) {
	console.log('No Argument');
} else {
	console.log(lol[2]);
}
