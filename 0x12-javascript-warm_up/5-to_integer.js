#!/usr/bin/node
const argument = parseInt(process.argv[2]);
if (process.argv[2] === undefined || isNaN(argument)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + argument);
}
