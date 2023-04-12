#!/usr/bin/node

/* This script will print two arguments passed to it, in the following format
  'is'
  example:
  ./4-concat.js c cool
  c is cool
  Not allowed to use `var`
*/

const arg1 = process.argv[2]; // get first string
const arg2 = process.argv[3]; // get second string

console.log(`${arg1} is ${arg2}`); // print using format
