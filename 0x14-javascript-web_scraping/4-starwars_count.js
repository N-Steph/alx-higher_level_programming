#!/usr/bin/node

const process = require('process');
const request = require('request');

const ID = '18';
const url = process.argv[2];
request(url, (error, response, body) => {
  if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let numberFilms = 0;
    for (const object of films) {
      for (const film of object.characters) {
        if (film === 'https://swapi-api.alx-tools.com/api/people/' + ID + '/') {
          numberFilms += 1;
        }
      }
    }
    console.log(numberFilms);
  } else {
    console.log(error);
  }
});
