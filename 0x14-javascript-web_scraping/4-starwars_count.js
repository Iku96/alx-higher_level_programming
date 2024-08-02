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
      const charID = '18';
      let count = 0;

      body.results.forEach(film => {
        // Extract character IDs from the URLs in the film.characters
        const characterIDs = film.characters.map(url => {
          const parts = url.split('/');
          return parts[parts.length - 2]; // Fetching the second last part which would be the ID
        });

        if (characterIDs.includes(charID)) {
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
