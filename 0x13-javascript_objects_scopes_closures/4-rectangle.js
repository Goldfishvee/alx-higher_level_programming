#!/usr/bin/node

/* This script will define additional properties of the rectangle
  constructor must take 2 arguments w and h
  if w or h is equal to 0 or not a positive integer, create an empty object
  An instance method called print() will print the rectangle using the character 'X'
  An instance method called rotate() will exchange the wdith and height of the rectangle
  An instance method called double() will multiply height and width by 2
*/

module.exports = class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
