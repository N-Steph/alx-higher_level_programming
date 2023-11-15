#!/usr/bin/env node
const { argv } = require('node:process');
const argument = parseInt(argv[2]);
if (argv[2] === undefined || isNaN(argument)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + argument);
}
