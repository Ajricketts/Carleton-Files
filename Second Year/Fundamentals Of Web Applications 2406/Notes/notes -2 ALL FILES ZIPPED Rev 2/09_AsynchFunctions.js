/*
Is it possible to have a single callback and chain the executions?
*/

function read(callback) {
  setTimeout(function() {
      console.log("read data")
      callback()
    },
    Math.floor((Math.random() * 1000) + 1))
}

function process(callback) {
  setTimeout(function() {
      console.log("process data")
      callback()
    },
    Math.floor((Math.random() * 1000) + 1))
}

function output(callback) {
  setTimeout(function() {
      console.log("output results")
      callback()
    },
    Math.floor((Math.random() * 1000) + 1))
}

read(process(output())) //<--- WILL THIS WORK -What is wrong here?
