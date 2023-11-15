#!/usr/bin/env node
const { argv } = require('node:process');
if (argv[2] === undefined || isNaN(parseInt(argv[2]))) {
  console.log('Missing number of occurences');
} else if (parseInt(argv[2]) > 0) {
  for (let i = 0; i < parseInt(argv[2]); i++) {
    console.log('C is fun');
  }
}
