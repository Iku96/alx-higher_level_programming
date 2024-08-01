#!/usr/bin/node

// Importing the fs module
const fs = require('fs');

// Getting the file path from the first argument
const filepath = process.argv[2];

// Reading the file with utf-8 encoding
fs.readFile(filepath, 'utf8', (err, data) => {
  if (err) {
    // If an error occurs, it will print the error obj
    console.log(err);
  } else {
    // If no errors occur, it will print the file content
    console.log(data);
  }
});
