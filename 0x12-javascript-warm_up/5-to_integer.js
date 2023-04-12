#!/usr/bin/node

/* This script will print 'My number: <first argument converted in integer>'
  if first argument can be converted to an integer
  if first argument cannot be converted, print "Not a number"
  Not allowed to use `var` or try/catch
*/

const input = process.argv[2];
const prsdInput = parseInt(input);

if (isNaN(prsdInput)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${prsdInput}`);
}
