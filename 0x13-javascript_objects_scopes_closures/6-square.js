#!/usr/bin/node

/* This script will define a square that inherits from a previous defined Square.
  An instance method called charPrint(c) will print the rectangle using the character 'c'
  if c is undefined, use the character X
*/

class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += c;
      }
      console.log(row);
    }
  }
}

module.exports = Square;
