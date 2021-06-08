/*
(c) 2018 LD Nel

Javasript to handle mouse dragging and release
to drag a string around the html canvas
Keyboard arrow keys are used to move a moving box around
(The mouse co-ordinates are wrong if the canvas is scrolled with scroll bars.
 Exercise: can you fix this?)

Here we are doing all the work with javascript and jQuery. (none of the words
are HTML, or DOM, elements. The only DOM element is just the canvas on which
where are drawing.

This example shows examples of using JQuery
JQuery syntax:
$(selector).action();
e.g.
$(this).hide() - hides the current element.
$("p").hide() - hides all <p> elements.
$(".test").hide() - hides all elements with class="test".
$("#test").hide() - hides the element with id="test".

Mouse event handlers are being added and removed using jQuery and
a jQuery event object is being passed to the handlers

Keyboard keyDown handler is being used to move a "moving box" around

Notice in the .html source file there are no pre-attached handlers.
*/

//Use javascript array of objects to represent words and their locations
const words = []
words.push({ word: "I", x: 50, y: 50 })
words.push({ word: "like", x: 70, y: 50 })
words.push({ word: "the", x: 120, y: 50 })
words.push({ word: "way", x: 170, y: 50 })
words.push({ word: "your", x: 230, y: 50 })
words.push({ word: "sparkling", x: 300, y: 50 })
words.push({ word: "earings", x: 430, y: 50 })
words.push({ word: "lay", x: 530, y: 50 })

let movingString = {
  word: "Moving",
  x: 100,
  y: 100,
  xDirection: 1, //+1 for leftwards, -1 for rightwards
  yDirection: 1, //+1 for downwards, -1 for upwards
  stringWidth: 50, //will be updated when drawn
  stringHeight: 24
} //assumed height based on drawing point size

//intended for keyboard control
let movingBox = {
  x: 50,
  y: 50,
  width: 100,
  height: 100
}

let timer //used to control the free moving word
let pollingTimer //timer to poll server for location updates

let wordBeingMoved //word being dragged by mouse
let wordTargetRect = {
  x: 0,
  y: 0,
  width: 0,
  height: 0
} //bounding box around word being targeted

let deltaX, deltaY //location where mouse is pressed
let canvas = document.getElementById("canvas1") //our drawing canvas
const fontPointSize = 18 //point size for word text
const wordHeight = 20 //estimated height of a string in the editor
const editorFont = "Arial" //font for your editor

function getWordAtLocation(aCanvasX, aCanvasY) {
  //locate the word targeted by aCanvasX, aCanvasY
  //find a word whose bounding box contains location (aCanvasX, aCanvasY)

  const context = canvas.getContext("2d");

  for (let i = 0; i < words.length; i++) {
    let wordWidth = context.measureText(words[i].word).width
    if (
      aCanvasX > words[i].x &&
      aCanvasX < words[i].x + wordWidth &&
      (aCanvasY > words[i].y - wordHeight && aCanvasY < words[i].y)
    ) {
      //set word targeting rectangle for debugging display
      wordTargetRect = {
        x: words[i].x,
        y: words[i].y - wordHeight,
        width: wordWidth,
        height: wordHeight
      }
      return words[i] //return the word found
    }
  }
}

function drawCanvas() {
  const context = canvas.getContext("2d");

  context.fillStyle = "white";
  context.fillRect(0, 0, canvas.width, canvas.height); //erase canvas

  context.font = "" + fontPointSize + "pt " + editorFont;
  context.fillStyle = "cornflowerblue";
  context.strokeStyle = "blue";

  for (let i = 0; i < words.length; i++) {
    let data = words[i]
    context.fillText(data.word, data.x, data.y);
    context.strokeText(data.word, data.x, data.y);
  }

  movingString.stringWidth = context.measureText(movingString.word).width;
  context.fillText(movingString.word, movingString.x, movingString.y);

  //draw moving box
  context.fillRect(movingBox.x, movingBox.y, movingBox.width, movingBox.height);

  //draw circle
  context.beginPath()
  context.arc(
    canvas.width / 2, //x co-ord
    canvas.height / 2, //y co-ord
    canvas.height / 2 - 5, //radius
    0, //start angle
    2 * Math.PI //end angle
  )
  context.stroke()

  //draw box around word last targeted with mouse -for debugging
  context.strokeStyle = "red";
  context.strokeRect(
    wordTargetRect.x,
    wordTargetRect.y,
    wordTargetRect.width,
    wordTargetRect.height
  )
}

function handleMouseDown(e) {
  //get mouse location relative to canvas top left
  let rect = canvas.getBoundingClientRect()
  //var canvasX = e.clientX - rect.left
  //var canvasY = e.clientY - rect.top
  let canvasX = e.pageX - rect.left //use  event object pageX and pageY
  let canvasY = e.pageY - rect.top
  console.log("mouse down:" + canvasX + ", " + canvasY)

  wordBeingMoved = getWordAtLocation(canvasX, canvasY)
  //console.log(wordBeingMoved.word)
  if (wordBeingMoved != null) {
    deltaX = wordBeingMoved.x - canvasX
    deltaY = wordBeingMoved.y - canvasY
    //attache mouse move and mouse up handlers
    $("#canvas1").mousemove(handleMouseMove)
    $("#canvas1").mouseup(handleMouseUp)
  }

  // Stop propagation of the event and stop any default
  //  browser action
  e.stopPropagation()
  e.preventDefault()

  drawCanvas()
}

function handleMouseMove(e) {
  console.log("mouse move");

  //get mouse location relative to canvas top left
  let rect = canvas.getBoundingClientRect()
  let canvasX = e.pageX - rect.left
  let canvasY = e.pageY - rect.top

  wordBeingMoved.x = canvasX + deltaX
  wordBeingMoved.y = canvasY + deltaY

  e.stopPropagation()

  drawCanvas()
}

function handleMouseUp(e) {
  console.log("mouse up")
  e.stopPropagation()

  //remove mouse move and mouse up handlers but leave mouse down handler
  $("#canvas1").off("mousemove", handleMouseMove); //remove mouse move handler
  $("#canvas1").off("mouseup", handleMouseUp); //remove mouse up handler

  drawCanvas() //redraw the canvas
}

//JQuery Ready function -called when HTML has been parsed and DOM
//created
//can also be just $(function(){...});
//much JQuery code will go in here because the DOM will have been loaded by the time
//this runs

function handleTimer() {
  movingString.x = movingString.x + 5 * movingString.xDirection
  movingString.y = movingString.y + 5 * movingString.yDirection

  //keep moving word within bounds of canvas
  if (movingString.x + movingString.stringWidth > canvas.width)
    movingString.xDirection = -1
  if (movingString.x < 0) movingString.xDirection = 1
  if (movingString.y > canvas.height) movingString.yDirection = -1
  if (movingString.y - movingString.stringHeight < 0)
    movingString.yDirection = 1

  drawCanvas()
}

//KEY CODES
//should clean up these hard coded key codes
const RIGHT_ARROW = 39
const LEFT_ARROW = 37
const UP_ARROW = 38
const DOWN_ARROW = 40

function pollingTimerHandler() {
  //console.log("poll server");
  let dataObj = {
    x: -1,
    y: -1
  } //used by server to react as poll
  //create a JSON string representation of the data object
  let jsonString = JSON.stringify(dataObj)

  //Poll the server for the location of the moving box
  //update the server with a new location of the moving box
  socket.emit('blueBoxData', jsonString)
}

function handleKeyDown(e) {
  console.log("keydown code = " + e.which);

  let dXY = 5; //amount to move in both X and Y direction
  if (e.which == UP_ARROW && movingBox.y >= dXY) movingBox.y -= dXY; //up arrow
  if (
    e.which == RIGHT_ARROW &&
    movingBox.x + movingBox.width + dXY <= canvas.width
  )
    movingBox.x += dXY; //right arrow
  if (e.which == LEFT_ARROW && movingBox.x >= dXY) movingBox.x -= dXY; //left arrow
  if (
    e.which == DOWN_ARROW &&
    movingBox.y + movingBox.height + dXY <= canvas.height
  )
    movingBox.y += dXY; //down arrow

  //upate server with position data
  //may be too much traffic?
  let dataObj = {
    x: movingBox.x,
    y: movingBox.y
  }
  //create a JSON string representation of the data object
  let jsonString = JSON.stringify(dataObj)

  //update the server with a new location of the moving box
  //update the server with a new location of the moving box
  socket.emit('blueBoxData', jsonString)
}

function handleKeyUp(e) {
  console.log("key UP: " + e.which)
  let dataObj = {
    x: movingBox.x,
    y: movingBox.y
  }
  //create a JSON string representation of the data object
  let jsonString = JSON.stringify(dataObj)

  $.post("positionData", jsonString, function(data, status) {
    console.log("data: " + data)
    console.log("typeof: " + typeof data)
    //do nothing;
  })
}

$(document).ready(function() {
  //add mouse down listener to our canvas object
  $("#canvas1").mousedown(handleMouseDown)
  //add keyboard handler to document
  $(document).keydown(handleKeyDown)
  $(document).keyup(handleKeyUp)

  timer = setInterval(handleTimer, 100) //tenth of second

  drawCanvas()
})

//connect to server and retain the socket
let socket = io('http://' + window.document.location.host)
//let socket = io('http://localhost:3000')

socket.on('blueBoxData', function(data) {
  console.log("data: " + data)
  console.log("typeof: " + typeof data)
  let locationData = JSON.parse(data)
  movingBox.x = locationData.x
  movingBox.y = locationData.y
  drawCanvas()
})
