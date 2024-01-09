#!/usr/bin/node

if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  let biggest = parseInt(process.argv[2], 10);
  let secondBiggest = biggest;
  for (let i = 3; i < process.argv.length; i++) {
    const number = parseInt(process.argv[i], 10);
    if (number > biggest) {
      secondBiggest = biggest;
      biggest = number;
    }
  }
  console.log(secondBiggest);
}
