#!/usr/bin/node
const argv = process.argv;
function factorial (number) {
  if (number <= 0) {
    return 1;
  }
  return number * factorial(number - 1);
}

const argument = parseInt(argv[2]);
if (argument === undefined || isNaN(argument)) {
  console.log(1);
} else {
  const answer = factorial(argument);
  console.log(answer);
}
