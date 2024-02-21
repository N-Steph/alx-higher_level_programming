#!/usr/bin/node

const fs = require('fs');

try {
  const content = fs.readFileSync(process.argv[2]);
  console.log(content.toString());
} catch (e) {
  console.log(e);
}
