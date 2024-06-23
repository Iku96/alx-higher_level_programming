#!/usr/bin/node

const process = require('process');

const args = process.argv;

const numbers = [];

if (args.length < 4) {
  console.log(0);
} else {
  for (let index = 2; index < args.length; index++) {
    numbers.push(parseInt(args[index]));
  }
  numbers.sort((a, b) => b - a);
  console.log(numbers[1]);
}
