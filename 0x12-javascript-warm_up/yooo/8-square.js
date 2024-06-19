#!/usr/bin/node

const size = parseInt(process.argv[2]);
if (isNaN(process.argv[2])) {
	console.log('Missing size');
} else {
	for (i = 0; i < size; i++) {
			console.log('X'.repeat(size));
	}
}
