#!/usr/bin/node

/* This script prints the addition of 2 integers
  function prototype: add(a, b)
  first argument is first integer. Second arg is secong int
*/

function add (a, b) {
  return (a + b);
}

const arg1 = process.argv[2];
const arg2 = process.argv[3];

const int1 = parseInt(arg1);
const int2 = parseInt(arg2);

const sum = add(int1, int2);

console.log(sum);
