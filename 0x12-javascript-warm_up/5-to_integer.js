#!/usr/bin/node
//coverts 1st arg to integer
const num = Number(process.argv[2]);
if (isNaN(num)) {
	console.log('Not a number');
} else {
	console.log('My number:', num);
}
