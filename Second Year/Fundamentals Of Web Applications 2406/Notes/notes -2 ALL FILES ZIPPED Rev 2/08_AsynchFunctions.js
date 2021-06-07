/*
MOST javascript node.js modules provide asynchronous functions that accept
a SINGLE callback parameter. That provides a standard (expected) approach

An important node.js convention is that functions only have ONE callback
function parameter
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

//HOW WOULD WE INVOKE THESE FUNCTIONS?
