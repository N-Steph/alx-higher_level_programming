#!/usr/bin/node
const Square0 = require('./5-square');
module.exports = class Square extends Square0 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === 'X' || c === undefined) {
      super.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          process.stdout.write(c);
        }
        process.stdout.write('\n');
      }
    }
  }
};
