#!/usr/bin/node
let counter = 0;
exports.logMe = function (item) {
  return console.log(`${counter++}: ${item}`);
};
