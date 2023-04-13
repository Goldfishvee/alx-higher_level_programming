#!/usr/bin/node

/* This function will convert anumber from base 10 to another base passed as an argument
   You are not allowed to import any file
   You are not allowed to declare any new variable (`var`, `let`, etc)
*/

exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
