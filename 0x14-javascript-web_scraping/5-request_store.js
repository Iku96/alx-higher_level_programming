#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const URL = process.argv[2];
const filepath = process.argv[3];

function starwars () {
  request(URL, (err, response, body) => {
    if (err) {
      console.error('Error fetching data:', err);
      return;
    }

    fs.writeFile(filepath, 'utf-8', body, (err) => {
      if (err) {
        console.error('Error writing to the file', err);
      }
    });
  });
}

starwars();
