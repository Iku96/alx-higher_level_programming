#!/usr/bin/node

const process = require('process');

const args = process.argv;

const toPrint = 'C is fun';

if (!isNaN(parseInt(args[2]))) {
  for (let index = 0; index < args[2]; index++) {
    console.log(toPrint);
  }
} else {
  console.log('Missing number of occurences');
}
