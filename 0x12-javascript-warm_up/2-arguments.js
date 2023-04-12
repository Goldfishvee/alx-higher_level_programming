#!/usr/bin/node
/* This script will print a message depending on the number of
   arguments passed.
   If no arguments are passed to the script, print "No argument"
   If only one argument is passed to the script, print "Argument found"
   Otherwise, print "Arguments found"
*/

const input = process.argv.slice(2); // read input from cmdline

if (input.length === 0) { // if no input
  console.log('No argument');
} else if (input.length === 1) { // if only 1 input
  console.log('Argument found');
} else { // if multiple input
  console.log('Arguments found');
}
