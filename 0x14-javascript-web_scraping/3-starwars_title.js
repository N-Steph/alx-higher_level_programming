#!/usr/bin/node

const request = require('request');

const starWarUrl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(starWarUrl, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const myData = JSON.parse(body);
    console.log(myData.title);
  }
});
