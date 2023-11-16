#!/usr/bin/node
function add (a, b) {
  const result = a + b;
  console.log(result);
}
const argv = process.argv;
if (argv.length > 2 && argv[2] !== undefined && argv[3] !== undefined &&
    !isNaN(parseInt(argv[2])) && !isNaN(parseInt(argv[3]))) {
  const a = parseInt(argv[2]);
  const b = parseInt(argv[3]);
  add(a, b);
} else {
  console.log('NaN');
}
