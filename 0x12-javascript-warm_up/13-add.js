#!/usr/bin/node

/* This script will return the addition of 2 integers using a function
  The function must be visible from outside
  Not allowed to use `var`
*/

const add = (a, b) => {
  return a + b;
};

module.exports = { add };
