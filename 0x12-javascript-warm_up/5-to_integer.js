#!/usr/bin/node

const process = require('process');

const args = process.argv;

if (!isNaN(parseInt(args[2]))) {
  console.log('My number: ' + args[2]);
} else {
  console.log('Not a number');
}
