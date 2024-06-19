#!/usr/bin/node

const process = require('process');

const args = process.argv;

if (args === 0) {
  console.log('No argument');
} else {
  console.log(args.at(2));
}
