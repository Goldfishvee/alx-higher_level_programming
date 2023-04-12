#!/usr/bin/node

/* This script will print the first argument passed to it.
  If no arguments are passed to the script, print "No argument".
  You are not allowed to use `var` nor `length`
*/

const input = process.argv[2];

if (input === undefined) { // no argument result in an undefined behav
  console.log('No argument');
} else {
  console.log(input);
}
