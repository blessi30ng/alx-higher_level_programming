#!/usr/bin/node
const lol = process.argv.length;
if (lol === 2) {
	console.log('No arguments');
} else if (lol === 3) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}
