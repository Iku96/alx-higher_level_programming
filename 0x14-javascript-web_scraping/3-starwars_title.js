#!/usr/bin/node

const request = require('request');

const movieID = process.argv[2];

function starwars () {
  const requestURL = `https://swapi-api.alx-tools.com/api/films/${movieID}/`;

  request(requestURL, { json: true }, (err, response, body) => {
    if (err) {
      console.error('Error fetching data:', err);
      return;
    }

    // Find the movie matching the episode ID.

    if (body && body.title) {
      console.log(body.title); // Prints the title of the movie
    } else {
      console.log('Movie not found');
    }
  });
}

starwars();
