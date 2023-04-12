#!/usr/bin/node

/* This script will print a square
  If the argument can't be converted to an integer, print
  "Missing size".
  You must use the character 'X' to print the square
  You must use a loop (while, for, etc.)
*/

const input = process.argv[2];
const parsedInpt = parseInt(input);

if (isNaN(parsedInpt)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parsedInpt; i++) {
    let row = '';
    for (let j = 0; j < parsedInpt; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
