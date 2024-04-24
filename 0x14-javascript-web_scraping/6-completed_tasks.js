#!/usr/bin/node

const process = require('process');
const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (response.statusCode === 200) {
    const data = JSON.parse(body);
    const taskCompleted = {};
    for (const user of data) {
      if (user.userId in taskCompleted) {
        if (user.completed) {
          taskCompleted[user.userId] += 1;
        }
      } else {
        if (user.completed) {
          taskCompleted[user.userId] = 1;
        }
      }
    }
    console.log(taskCompleted);
  } else {
    console.log(error);
  }
});
