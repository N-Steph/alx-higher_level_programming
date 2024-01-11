#!/usr/bin/node
let callNumber = 0;

exports.logMe = function (item) {
  console.log(callNumber + ': ' + item);
  callNumber += 1;
};
