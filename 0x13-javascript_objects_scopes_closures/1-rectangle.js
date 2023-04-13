#!/usr/bin/node

/* This script will define a rectangle
  constructor must take two arguments w and h
  width attribute will be initialized with the value of w
  height attribute will be initialized with the value of h
*/

module.exports = class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
};
