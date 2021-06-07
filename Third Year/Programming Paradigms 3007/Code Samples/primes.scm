#|
Author: Andrew Runka
Student #: 100123456

This is an example piece of code for demonstration of documentation and testing standards.
Ensure lang is set to R5RS to run.
|#


;The Sieve of Eratosthanes is a method for determining prime numbers. 
;	This program implements the Sieve of Eratosthanes to return a list of the first n prime numbers
; Input: integer -> number of primes to return
; Output: list of prime numbers of length n
(define (sieve n)
    
  ;main loop, count up to n primes
  (define (iter i primes)
    (cond ((= (length primes) n) primes)
          ((divisBy primes i) (iter (+ i 1) primes))
          (else (iter (+ i 1)(append primes (list i))))))

  ;compare the value i against a list of primes, true if any of them divide evenly
  (define (divisBy l i)
    (not (= (length (filter l (lambda (x) (= (modulo i x) 0)))) 0)))

  ;filters a list of values using a given predicate
  (define (filter lis pred)
    (cond ((null? lis) lis)
          ((pred (car lis)) (cons (car lis)(filter (cdr lis) pred)))
          (else (filter (cdr lis) pred))))

  (if (< n 1)        ;edge checking
      '()
      (iter 2 '()))) ; begin the loop
    
        
;Testing

;simple cases
(display "(sieve 5)=> ")(newline)
   (display "Expected: (2 3 5 7 11)")(newline)
   (display "Actual: ")(sieve 5)(newline)

(display "(sieve 10)=> ")(newline)
   (display "Expected: (2 3 5 7 11 13 17 19 23 29)")(newline)
   (display "Actual: ")(sieve 10)(newline)

;edge case
(display "(sieve 1)=> ")(newline)
   (display "Expected: (2)")(newline)
   (display "Actual: ")(sieve 1)(newline)

;large number
(display "(sieve 50)=> ")(newline)
   (display "Expected: a long list (2 ... 229)")(newline)
   (display "Actual: ")(sieve 50)(newline)

;outside cases
(display "(sieve 0)=> ")(newline)
   (display "Expected: () ")(newline)
   (display "Actual: ")(sieve 0)(newline)
(display "(sieve -1)=> ")(newline)
   (display "Expected: ()")(newline)
   (display "Actual: ")(sieve -1)(newline)
