#!/usr/bin/node
const list = require('./100-data').list;

let i = 0;
function index (x) {
  const result = x * i;
  i += 1;
  return result;
}
const newList = list.map(index);
console.log(list);
console.log(newList);
