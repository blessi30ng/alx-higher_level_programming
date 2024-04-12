#!/usr/bin/node
// prints factorial
function factorial (num) {
	if (num > 1) {
		return num * factorial(num - 1);
	} else {
		return 1;
	}
}
const n = Number(process.argv[2]);
console.log(factorial(n));
