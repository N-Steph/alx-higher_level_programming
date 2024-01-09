#!/usr/bin/node

function add (a, b) {
  const result = a + b;
  console.log(result);
}

add(parseInt(process.argv[2], 10), parseInt(process.argv[3]));
