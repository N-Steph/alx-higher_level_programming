#!/usr/bin/node
const { argv } = require('node:process');
for (let i = 0; i < 2; i++) {
  argv.shift();
}
if (argv[0] === undefined) {
  console.log('No argument');
} else {
  console.log(argv[0]);
}
