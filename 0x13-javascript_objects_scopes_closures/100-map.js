#!/usr/bin/node
const list = require('./100-data').list;

let i = -1;
const newList = list.map((x) => x * list.indexOf(x, i + 1));
console.log(list);
console.log(newList);
