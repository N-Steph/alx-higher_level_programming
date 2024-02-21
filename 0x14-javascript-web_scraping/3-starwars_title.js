#!/usr/bin/node

const request = require('request');

const starWarUrl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(starWarUrl, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const info = JSON.parse(body);
    console.log(info.title);
  }
});
