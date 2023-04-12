#!/usr/bin/node

/* This script will search for the second biggest integer in the list of args
  All arguments can be converted to integer
  Not allowed to use `var`
*/

const args = process.argv.slice(2);

if (args.length < 2) {
  console.log(0);
} else {
  const intArgs = args.map(Number); // cast into integer
  const sortArgs = intArgs.sort((a, b) => b - a); // sort in desc order
  console.log(sortArgs[1]);
}
