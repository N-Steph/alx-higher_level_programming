#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const dataParse = JSON.parse(body);
    const userTaskCompleted = {};
    for (const task of dataParse) {
      if (task.completed && task.userId in userTaskCompleted) {
        userTaskCompleted[task.userId] += 1;
      } else if (task.completed && !(task.userId in userTaskCompleted)) {
        userTaskCompleted[task.userId] = 1;
      }
    }
    console.log(userTaskCompleted);
  }
});
