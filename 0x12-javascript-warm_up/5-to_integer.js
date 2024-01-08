#!/usr/bin/node
const { argv } = require('node:process');

if (argv.length === 2) {
  console.log('Not a number');
} else {
  const convertNumber = Number(argv[2]);
  if (convertNumber === 'NaN') {
    console.log('Not a number');
  } else {
    console.log('My number:', Math.floor(convertNumber));
  }
}
