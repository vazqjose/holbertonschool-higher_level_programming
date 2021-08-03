#!/usr/bin/node

const process = require('process');
const argv = process.argv;
const x = parseInt(argv[2]);
let i = 0;
let j = 0;
let square = '';

if (x) {
  for (i = 0; i < x; i++) {
    for (j = 0; j < x; j++) {
      square += 'X';
    }
    console.log(square);
    square = '';
  }
} else {
  console.log('Missing size');
}
