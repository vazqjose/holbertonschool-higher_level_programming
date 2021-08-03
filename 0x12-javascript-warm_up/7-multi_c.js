#!/usr/bin/node

const process = require('process');
const argv = process.argv;
const x = parseInt(argv[2]);
let i = 0;

if (x) {
  for (i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
