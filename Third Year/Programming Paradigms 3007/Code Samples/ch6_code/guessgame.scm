(#%require (only racket/base random))

(define (guessgame)
  (define (iter soln)
    (let ((guess (getInput)))
      (if (not (compare guess soln))
          (iter soln))))
  
  (define (getInput)
    (newline)(display "Guess a number (1-10): ")
    (read))
  
  (define (compare x y)
    (cond ((= x y) (display "You got it!")(newline) #t)
          ((< x y) (display "Too low!") #f)
          (else (display "Too high!")#f)))

  (iter (+ 1 (random 10))))

(guessgame) 