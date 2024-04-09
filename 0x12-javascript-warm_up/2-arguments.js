#!/usr/bin/node
const lol = process.argv.length - 2;
if (lol === 0) {
	console.log('No arguments');
} else if (lol === 1) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}
