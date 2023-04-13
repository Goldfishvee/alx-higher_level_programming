#!/usr/bin/node

/* This script will print the number of arguments already printed and the new argument value
   Output format: <number of arguments already printed>: <current argument value>
   Example - 0: arg1
             1: arg2
*/

let count = 0;

exports.logMe = function (item) {
  console.log(count + ': ' + item);
  count++;
};
