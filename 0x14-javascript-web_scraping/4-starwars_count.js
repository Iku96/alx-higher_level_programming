#!/usr/bin/node

const request = require('request');

const URL = process.argv[2];

function starwars () {
  request(URL, { json: true }, (err, response, body) => {
    if (err) {
      console.error('Error fetching data:', err);
      return;
    }

    if (body && body.results) {
      const charURL = 'https://swapi-api.alx-tools.com/api/people/18/';
      let count = 0;

      body.results.forEach(film => {
        if (film.characters.includes(charURL)) {
          count++;
        }
      });
      console.log(count);
    } else {
      console.log('No films found or the API response was invalid.');
    }
  });
}

starwars();
