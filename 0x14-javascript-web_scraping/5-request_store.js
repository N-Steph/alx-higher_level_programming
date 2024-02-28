#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];
request(url, function (error, response, data) {
  if (!error && response.statusCode === 200) {
    fs.writeFile(filePath, data, { encoding: 'UTF-8' {, function (error) {
      if (error) {
        console.log(error);
      }
    });
  }
});
