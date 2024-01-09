#!/usr/bin/node

if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else if (process.argv.length === 4) {
  if (parseInt(process.argv[2]) > parseInt(process.argv[3])) {
    console.log(parseInt(process.argv[3]));
  } else {
    console.log(parseInt(process.argv[2]));
  }
} else {
  let biggest = parseInt(process.argv[2], 10);
  let secondBiggest = biggest;
  for (let i = 3; i < process.argv.length; i++) {
    const number = parseInt(process.argv[i], 10);
    if (number > biggest) {
      biggest = number;
    }
  }
  for (let i = 3; i < process.argv.length; i++) {
    const number = parseInt(process.argv[i], 10);
    if (number === biggest) {
      continue;
    } else if (number > secondBiggest) {
      secondBiggest = number;
    }
  }
  console.log(secondBiggest);
}
