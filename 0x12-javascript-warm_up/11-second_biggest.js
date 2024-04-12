#!/usr/bin/node
// return 2nd biggest number
const arg = [];
for (let i = 0; i < process.argv.length - 2; i++) {
	arg[i] = Number(process.argv[i + 2]);
}

const filtered = arg.filter(n => !isNaN(n));
const sorted = filtered.sort(function(a, b) {
	return a - b;
});

if (sorted.length < 2) {
	console.log(0);
} else {
	console.log(sorted[sorted.length -2]);
}
