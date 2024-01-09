#!/usr/bin/node

const number = Number(process.argv[2]);

if (isNaN(number)) {
  console.log('Missing number of occurences');
} else {
  if (number > 0) {
    for (let i = 0; i < number; i++) {
      console.log('C is fun');
    }
  }
}
