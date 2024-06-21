#!/usr/bin/node

exports.esrever = function (list) {
  for (let index = 0; index < list.length / 2; index++) {
    const temp = list[index];
    list[index] = list[list.length - index - 1];
    list[list.length - index - 1] = temp;
  }
  return list;
};
