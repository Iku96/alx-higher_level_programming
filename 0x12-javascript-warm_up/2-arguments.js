#!/usr/bin/node

// Importing the process module
const process = require('process');

const args = process.argv;

if (args.length === 2) {
  console.log('No arguments found');
} else if (args.length === 3) {
  console.log('One argument found');
} else {
  console.log('Arguments found');
}
