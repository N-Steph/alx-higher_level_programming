#!/usr/bin/node

const process = require('process');
const fs = require('fs');

fs.readFile(process.argv[2], (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data.toString());
  }
});
