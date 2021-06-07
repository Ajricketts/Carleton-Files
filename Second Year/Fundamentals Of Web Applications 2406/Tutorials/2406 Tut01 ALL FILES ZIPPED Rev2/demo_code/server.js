/*
COMP 2406
(c) 2018 Louis D. Nel

Example Simple Server that is prepared to receive GET and POST HTTP requests.
GET requests handle the URL requests from a browser.
POST requests are intended to handle form data.

Launch servcer with
node server.js

Testing:
Use browser to view pages at
http:localhost:3000
http:localhost:3000/
http://localhost:3000/index.html

Cntl+C in console to stop server.
*/


const http = require("http") //needed for http communication
const url = require("url") //used to parse url strings

let visitorCounter = 0

http.createServer(function(request, response) {
  let urlObj = url.parse(request.url, true, false)
  console.log("\n============================")
  console.log("PATHNAME: " + urlObj.pathname)
  console.log("METHOD: " + request.method)

  let receivedData = ''

  //Event handler to collect message data that might
  //arrive in chunks (several smaller TCP/IP messages)

  request.on("data", function(chunk) {
    receivedData += chunk
  })

  //Event handler for the end of the message data
  request.on("end", function() {
      console.log("received data: ", receivedData)
      console.log("type: ", typeof receivedData)

      visitorCounter++

      if (request.method === "GET") {
        //Handle HTTP GET requests from browser
        if (urlObj.pathname === "/" || urlObj.pathname === "/index.html") {
          //ROUTE / or /index.html
          response.writeHead(200, {
            "Content-Type": "text/html"
          })
          response.write('<!DOCTYPE html>')
          response.write('<html>')
          response.write('<head>')
          response.write('</head>')
          response.write('<body>')
          response.write('<h1>Hello World</h1>')
          response.write('<p>Greetings COMP 2406</p>')
          response.write(`<p>You are visitor ${visitorCounter}</p>`)
          response.write('</body>')
          response.write('</html>')
        } else {
          //ROUTE unknown
          response.writeHead(404)
          response.write("ERROR: PAGE NOT FOUND")
        }

        response.end() //send response to client
      } //end get

    //if it is a POST request then echo back the data.
    if (request.method === "POST") {
      //Handle POST requests
      console.log(`POST receivedData: ${receivedData}`)

      //respond to client
      response.writeHead(200, {
        "Content-Type": 'text/html'
      })
      response.write('<!DOCTYPE html>')
      response.write('<html><head></head><body><p>Thanks for your request</p></body></html>')
      response.end() //send just the JSON object as plain text
    } //post
  }) //request on
}).listen(3000)

console.log("Server Running at PORT 3000  CNTL-C to quit")
console.log("To Test:")
console.log("http://localhost:3000")
console.log("http://localhost:3000/")
console.log("http://localhost:3000/index.html")
