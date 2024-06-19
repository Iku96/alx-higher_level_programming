#!/usr/bin/node

const process = require('process');

const args = process.argv;

console.log(args.at(2) + ' is ' + args.at(3));
