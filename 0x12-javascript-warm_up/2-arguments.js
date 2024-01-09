#!/usr/bin/node
// const { argv } = require('node:process');
// const argv = require('node:process').argv;

if (process.argv.length === 2) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
