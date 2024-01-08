#!/usr/bin/node
const { argv } = require('node:process');

function factorial (a) {
  if (a === 0 || isNaN(a)) {
    return 1;
  }
  return a * factorial(a - 1);
}

console.log(factorial(parseInt(argv[2], 10)));
