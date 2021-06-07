/*
(c) 2018 LD Nel
To test:
Open two browsers at http://localhost:3000/canvasWithTimer.html

//collaboration through polling
//=============================

When the blue cube is moved with the arrow keys, a POST message will be
sent to the server when the arrow key is released, also while the key is
held down.

Clients also request the position of the movingBox by polling the server.
The smoothness is thus affected by the rate at which the polling timer
runs. The trade off is smooth behaviour vs. network traffic.

This polling app is a great candidate to use web sockets instead of polling.

Only the client moving the box will drop waypoints, the other clients don't
see the local waypoints, just their own.
*/

//Cntl+C to stop server

const app = require('http').createServer(handler)
const io = require('socket.io')(app) // wrap server app in socket io capibility
const fs = require("fs") //need to read static files
const url = require("url") //to parse url strings
const PORT = process.env.PORT || 3000 // useful if you want to specify port through environment variable

//server maintained location of moving box
let movingBoxLocation = {
  x: 100,
  y: 100
} //will be over-written by clients

const ROOT_DIR = "html" //dir to serve static files from

const MIME_TYPES = {
  css: "text/css",
  gif: "image/gif",
  htm: "text/html",
  html: "text/html",
  ico: "image/x-icon",
  jpeg: "image/jpeg",
  jpg: "image/jpeg",
  js: "application/javascript",
  json: "application/json",
  png: "image/png",
  svg: "image/svg+xml",
  txt: "text/plain"
}

app.listen(PORT) // start server listening on PORT

function get_mime(filename) {
  for (let ext in MIME_TYPES) {
    if (filename.indexOf(ext, filename.length - ext.length) !== -1) {
      return MIME_TYPES[ext]
    }
  }
  return MIME_TYPES["txt"]
}

function handler(request, response) {
    let urlObj = url.parse(request.url, true, false)
    console.log("\n============================")
    console.log("PATHNAME: " + urlObj.pathname)
    console.log("REQUEST: " + ROOT_DIR + urlObj.pathname)
    console.log("METHOD: " + request.method)

    let receivedData = ""

    //attached event handlers to collect the message data
    request.on("data", function(chunk) {
      receivedData += chunk
    })

    //event handler for the end of the message
    request.on("end", function() {
      console.log("REQUEST END: ")
      console.log("received data: ", receivedData)
      console.log("type: ", typeof receivedData)

      //if it is a POST request then echo back the data.
      /*
		A post message will be interpreted as either a request for
		the location of the moving box, or the location of the moving box
		being set by a client.
		If the .x and .y attributes are >= 0
		treat it as setting the location of the moving box.
		If the .x and .y attributes are < 0 treat it as a request (poll)
		for the location of the moving box.
		In either case echo back the location of the moving box to whatever client
		sent the post request.

		Can you think of a nicer API than using the numeric value of .x and .y
		to indicate a set vs. get of the moving box location.
		*/
      if (request.method == "POST") {
      }

      if (request.method == "GET") {
        //handle GET requests as static file requests
        fs.readFile(ROOT_DIR + urlObj.pathname, function(err, data) {
          if (err) {
            //report error to console
            console.log("ERROR: " + JSON.stringify(err))
            //respond with not found 404 to client
            response.writeHead(404)
            response.end(JSON.stringify(err))
            return
          }
          response.writeHead(200, {
            "Content-Type": get_mime(urlObj.pathname)
          })
          response.end(data)
        })
      }
    })
  }


  io.on('connection', function(socket){
    socket.on('blueBoxData', function(data){
      console.log('RECEIVED BOX DATA: ' + data)
      //to broadcast message to everyone including sender:
      io.emit('blueBoxData', data) //broadcast to everyone including sender
    })
  })

console.log("Server Running at PORT: 3000  CNTL-C to quit")
console.log("To Test:")
console.log("Open several browsers at: http://localhost:3000/canvasWithTimer.html")
