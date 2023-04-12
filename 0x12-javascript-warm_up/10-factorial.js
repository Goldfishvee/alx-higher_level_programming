#!/usr/bin/node

/* This script will compute and print a factorial
  factorial of NaN is 1. Use a function and do it recursively
*/

function factorial (num) {
  if (isNaN(num)) {
    return (1);
  } else if (num <= 1) {
    return (1);
  } else {
    return (num * factorial(num - 1));
  }
}

const arg1 = process.argv[2];
const num = parseInt(arg1);

const result = factorial(num);

console.log(result);
