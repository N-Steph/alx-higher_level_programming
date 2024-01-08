#!/usr/bin/node
const { argv } = require('node:process');

if (argv.length === 2 || argv.length === 3) {
  console.log(0);
} else {
  let biggest = parseInt(argv[2], 10);
  let secondBiggest = biggest;
  for (let i = 3; i < argv.length; i++) {
    const number = parseInt(argv[i], 10);
    if (number > biggest) {
      secondBiggest = biggest;
      biggest = number;
    }
  }
  console.log(secondBiggest);
}
