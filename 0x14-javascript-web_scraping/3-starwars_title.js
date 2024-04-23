#!/usr/bin/node

const process = require('process');
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, (error, response, body) => {
  if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  } else {
    console.log(error);
  }
});
