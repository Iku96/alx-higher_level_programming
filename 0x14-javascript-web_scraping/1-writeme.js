#!/usr/bin/node

// Importing the fs module
const fs = require('fs');

// Getting the file path from the first argument
const filepath = process.argv[2];
// Getting the string to write from the 2nd argument
const content = process.argv[3];

// Reading the file with utf-8 encoding
fs.writeFile(filepath, content, 'utf8', (err) => {
  if (err) {
    // If an error occurs, it will print the error obj
    console.log(err);
  }
});
