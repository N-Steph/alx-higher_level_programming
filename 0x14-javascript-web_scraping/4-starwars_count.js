#!/usr/bin/node
const request = require('request');

const urlFilms = process.argv[2];
const ID = '18';

request(urlFilms, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const jsonString = JSON.parse(body);
    const movieList = jsonString.results;
    let numberOfMovies = 0;

    for (const movie of movieList) {
      const allCharacters = movie.characters;
      for (const character of allCharacters) {
        if (character.includes(ID)) {
          numberOfMovies++;
        }
      }
    }
    console.log(numberOfMovies);
  }
});
