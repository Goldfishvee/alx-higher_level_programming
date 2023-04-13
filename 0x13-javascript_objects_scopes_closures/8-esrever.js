#!/usr/bin/node

/* This script will return a reversed list
   You are not allowed to use the built-in method `reverse`
*/

exports.esrever = function (list) {
  const reversedList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }
  return reversedList;
};
