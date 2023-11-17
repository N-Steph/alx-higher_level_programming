#!/usr/bin/node
const list = require('./100-data').list;

const list2 = list.map((x, index) => {
  if (index === 0 && x < 0) {
    return x * -1 * index;
  } else {
    return x * index
  }
});
console.log(list);
console.log(list2);
