#!/usr/bin/node

/* This script will import the rectangle module for the Square class
  The constructor will take only one argument: size
*/
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
