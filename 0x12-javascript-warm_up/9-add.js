#!/usr/bin/node

const process = require('process');
const argv = process.argv;
const a = parseInt(argv[2]);
const b = parseInt(argv[3]);

function add (a, b) {
  console.log(a + b);
}

if (a && b) {
  add(a, b);
} else {
  console.log('NaN');
}
