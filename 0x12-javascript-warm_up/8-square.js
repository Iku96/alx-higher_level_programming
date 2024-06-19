#!/usr/bin/node

const process = require('process');

const args = process.argv;

const toPrint = 'X';

if (!isNaN(parseInt(args[2]))) {
  for (let row = 0; row < args[2]; row++) {
    let square = '';
    for (let column = 0; column < args[2]; column++) {
      square += toPrint;
    }
    console.log(square);
  }
} else {
  console.log('Missing size');
}
