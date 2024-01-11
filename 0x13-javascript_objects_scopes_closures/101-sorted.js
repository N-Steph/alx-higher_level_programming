#!/usr/bin/node
const dict = require('./101-data').dict;

const newDict = {};
const dictKey = Object.keys(dict);

for (let i = 0; i < dictKey.length; i++) {
  const key = dictKey[i];
  const myArray = [];
  for (let j = 0; j < dictKey.length; j++) {
    if (dict[key] === dict[dictKey[j]]) {
      myArray.push(dictKey[j]);
    }
  }
  newDict[dict[key]] = myArray;
}

console.log(newDict);
