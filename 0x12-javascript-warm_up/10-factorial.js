#!/usr/bin/node

const process = require('process');
const argv = process.argv;
const a = parseInt(argv[2]);

if (a) {
  console.log(factorial(a));
} else {
  console.log(1);
}

function factorial (a) {
  if (a < 0) {
    return (-1);
  } else if (a === 0) {
    return (1);
  } else {
    return (a * factorial(a - 1));
  }
}
