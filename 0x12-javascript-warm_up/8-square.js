#!/usr/bin/node

const number = parseInt(process.argv[2], 10);

if (isNaN(number)) {
  console.log('Missing size');
} else {
  if (number > 0) {
    for (let i = 0; i < number; i++) {
      for (let j = 0; j < number; j++) {
        process.stdout.write('X');
      }
      console.log();
    }
  }
}
