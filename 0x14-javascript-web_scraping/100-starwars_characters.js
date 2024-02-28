#!/usr/bin/node
const request = require('request');

const urlFilm = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2] + '/';
const urlAllCharacters = 'https://swapi-api.alx-tools.com/api/people/';

for (let i = 1; i < 9; i++) {
  const url = urlAllCharacters + '?page=' + i;
  request(url, function (error, response, body) {
    if (!error && response.statusCode === 200) {
      const people = JSON.parse(body).results;
      for (const person of people) {
        const movies = person.films;
        for (const film of movies) {
          if (film === urlFilm) {
            console.log(person.name);
            break;
          }
        }
      }
    }
  });
}
