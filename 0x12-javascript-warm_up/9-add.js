#!/usr/bin/node
const { argv } = require('node:process');

function add (a, b) {
  const result = a + b;
  console.log(result);
}

add(parseInt(argv[2], 10), parseInt(argv[3]));
