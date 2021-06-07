(define (sqrt x)

  (define (square y)
    (* y y))
  (define (good-enough? guess)
    (let ((precision 0.001)
          (diff (abs (- (square guess) x))))
      (< diff precision)))
    
  (define (average x y)
    (/ (+ x y) 2))
  (define (improve guess)
    (average guess (/ x guess)))
  (define (sqrt-iteration guess)
    (if (good-enough? guess)
        guess
        (sqrt-iteration (improve guess))))
		

  (sqrt-iteration 1.0))