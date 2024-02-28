#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const jsonString = JSON.parse(body);
    console.log(jsonString.title);
  }
});
