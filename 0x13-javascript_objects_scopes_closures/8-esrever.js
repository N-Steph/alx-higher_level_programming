#!/usr/bin/node
exports.esrever = function (list) {
  const reverseList = [];
  if (list.length !== 0) {
    for (let i = list.length - 1; i >= 0; i--) {
      reverseList.push(list[i]);
    }
  }
  return reverseList;
};
