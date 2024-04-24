#!/usr/bin/node

const process = require('process');
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2] + '/';
request(url, (error, response, body) => {
  if (response.statusCode === 200) {
    const charactersUrl = JSON.parse(body).characters;
    for (const charUrl of charactersUrl) {
      request(charUrl, (error, response, body) => {
        if (response.statusCode === 200) {
          const characterName = JSON.parse(body).name;
          console.log(characterName);
        } else {
          console.log(error);
        }
      });
    }
  } else {
    console.log(error);
  }
});
