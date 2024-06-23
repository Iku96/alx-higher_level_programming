#!/usr/bin/node

const process = require('process');

const args = process.argv;

function add (a, b) {
  return parseInt(a) + parseInt(b);
}

const sum = add(args[2], args[3]);
console.log(sum);
