#!/usr/bin/node

/* This script will print 'x' times "C is fun"
  'x' is the first argument of the script
  If the argument can't be converted to an integer, print
  "Missing number of occurrences".
  You can only use two console.log
  You must use a loop (while, for, etc.)
*/

const input = process.argv[2];
const parsedInpt = parseInt(input);

if (isNaN(parsedInpt)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < parsedInpt; i++) {
    console.log('C is fun');
  }
}
