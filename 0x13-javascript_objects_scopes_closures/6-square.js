#!/usr/bin/node
const Square_ = require('./5-square');

module.exports = class Square extends Square_ {
  print (c = 'X') {
    for (let i = 0; i < this.width; i++) {
      for (let j = 0; j < this.height; j++) {
        process.stdout.write(c);
      }
      console.log();
    }
  }

  charPrint (c) {
    if (typeof (c) === 'undefined') {
      this.print();
    } else {
      this.print(c);
    }
  }
};
