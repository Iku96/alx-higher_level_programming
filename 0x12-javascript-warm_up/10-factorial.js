#!/usr/bin/node

const process = require('process');

const args = process.argv;

function factorial (number) {
  if (number === 0) {
    return 1;
  } else {
    return number * factorial(number - 1);
  }
}

console.log(factorial(parseInt(args[2])));
