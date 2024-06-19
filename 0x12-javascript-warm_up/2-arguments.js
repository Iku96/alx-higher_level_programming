#!/usr/bin/node

// Importing the process module
const process = require('process');

const args = process.argv;

if (args.length === 0) {
  console.log('No arguments found');
} else if (args.length === 1) {
  console.log('One argument found');
} else {
  console.log('Arguments found');
}
