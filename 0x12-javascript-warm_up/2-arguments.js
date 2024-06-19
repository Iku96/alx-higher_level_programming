#!/usr/bin/node

// Importing the process module
const process = require('process');

const args = process.argv;

if (args === 0) {
  console.log('No arguments found');
} else if (args === 1) {
  console.log('One argument found');
} else {
  console.log('Arguments found');
}
