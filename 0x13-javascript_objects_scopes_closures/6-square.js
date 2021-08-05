#!/usr/bin/node

/*
  Write a class Square that defines a square and inherits from Square of 5-square.js:
   -You must use the class notation for defining your class and extends
   -Create an instance method called charPrint(c) that prints the rectangle using the character c
   -If c is undefined, use the character X
*/

const MySquare = require('./5-square.js');

module.exports = class Square extends MySquare {
  charPrint (c) {
    let line = '';

    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        line += c;
      }
      console.log(line);
      line = '';
    }
  }
};
