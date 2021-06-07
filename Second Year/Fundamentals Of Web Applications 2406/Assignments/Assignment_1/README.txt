Author: Alyxander-Jacob Ricketts
Student Id: 101084146
Email: aj.ricketts@carleton.ca

Node version: v10.15.0
Npm version: v6.4.1

Install: The only thing needed to install to run this app is node and npm. Node.js can be downloaded at https://nodejs.org/en/.
          npm is packaged with Node.js

Launch: To launch app, navigate to /Assignment_1 and run:   node server.js and follow the TO TEST instructions in the console
        (visit http://localhost:3000/Assignment1.html in browser)

Issues:
        - Was not able to isolate the chords from the words if they are in the middle of the word so if there is a chord in the
        middle of the word then the whole word changes to green

        - Was not able to implement the transpose up or down because of this (chords are not separate from the words)

        - The Spacing on the canvas is a little off because I set the x and the y values in the server and not in the client
          (Realized this was a mistake but did not have time to change it)

        - Song lyrics under the canvas is not printed as nicely as in the example
