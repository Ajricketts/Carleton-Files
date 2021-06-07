/*
Asynch functions with for-loop using let

FOR-LOOPS in javascript using let variables
(ES6) attempt to do this better (as in more what the
programmer might have expected)

WITH LET: the value of i when the asynch function runs will be
the value that i had when the asynch function was CALLED
*/


for( let i = 0; i<10; i++){
  setTimeout(function() {
    console.log(i)
  }, 1000)
}

//GUESS THE OUTPUT
