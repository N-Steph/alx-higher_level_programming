#!/usr/bin/node
const argv = process.argv;
if (argv.length === 2 || argv.length === 3) {
  console.log(0);
} else {
  const intList = [];
  for (let i = 2; i < argv.length; i++) {
    intList.push(parseInt(argv[i]));
  }
  let biggestNumber = intList[0];
  let smallestNumber = intList[0];
  for (let i = 0; i < intList.length; i++) {
    if (intList[i] > biggestNumber) {
      biggestNumber = intList[i];
    }
    if (intList[i] < smallestNumber) {
      smallestNumber = intList[i];
    }
  }
  let smallestGap = biggestNumber - smallestNumber;
  for (let i = 0; i < intList.length; i++) {
    const gap = biggestNumber - intList[i];
    if (gap < smallestGap && gap !== 0) {
      smallestGap = gap;
    }
  }
  console.log(biggestNumber - smallestGap);
}
