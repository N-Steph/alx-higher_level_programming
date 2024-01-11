#!/usr/bin/node
const fs = require('fs');

// Reading first file
fs.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) throw err;
  // Reading second file
  fs.readFile(process.argv[3], 'utf-8', (err, data1) => {
    if (err) throw err;
    const value = data.toString() + data1.toString();
    // writing the content of first and second file to a third
    fs.writeFile(process.argv[4], value, (err) => {
      if (err) throw err;
    });
  });
});
