/*
Closures and for-loops have caused many problems in javascript
See the difference here between var and let in for-loop header
*/

var funcs = [];

console.log("-----------")
for (var i = 0; i < 10; i++) { //<-uses var variable
  funcs[i] = function() {
    console.log(i)
  }
}

funcs[0]()
funcs[3]()
funcs[9]()

//"fixed version with var in for-loop header"
//here we establish a closure around each value of i
console.log("-----------")
for (var i = 0; i < 10; i++) {  //<-uses var variable
  (function(x) {
    funcs[i] = function() {
      console.log(x)
    }
  })(i)
}

funcs[0]()
funcs[3]()
funcs[9]()

/*
Using the let var seems to establish a closure for each
value of i
*/
console.log("-----------")
for (let i = 0; i < 10; i++) { //<-uses let variable
  funcs[i] = function() {
    console.log(i)
  }
}

funcs[0]()
funcs[3]()
funcs[9]()
console.log("-----------")
