#!/usr/bin/node

// import the request module
const request = require('request');

// first argument is the URL you wanna send a GET request to
const url = process.argv[2];

// Capture error and display status code
request.get(url, (err, response) => {
  if (err) {
    console.log(err);
  } else {
    console.log('code:', response.statusCode);
  }
});
