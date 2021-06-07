/*
FOR-LOOP HELL: Asynchronous functions with for-loops using var

FOR-LOOPS in javascript using var variables.
var counter variables that use asynch functions have caused MANY problems

WITH VAR: the value of i when the asynch function runs will be
the value that i at the time the asynch function RUNS
*/


for( var i = 0; i<10; i++){
  setTimeout(function() {
    console.log(i)
  }, 1000)
}

//GUESS THE OUTPUT
