#!/usr/bin/node

const fs = require('fs');
const process = require('process');
const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (response.statusCode === 200) {
    fs.writeFile(process.argv[3], body.toString(), (err) => {
      console.log(err);
    });
  } else {
    console.log(error);
  }
});
