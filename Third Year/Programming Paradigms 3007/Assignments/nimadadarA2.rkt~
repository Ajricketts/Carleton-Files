#| Nima Dadar 100898748 |#

#| Q1a  Newton's method for cube roots is based on the fact that if y is an approximation to the cube root of x,
then a better approximation is given by the value: (x/y2+2y)/3
Use this formula to implement a cube-root procedure analogous to the square-root procedure from the lecture notes.
Your code should use nested functions and free variables wherever possible. |#

(define (cbrt x)
	(define (cube y)(* y y y))

	(define (good-enough? guess x)
		(< (abs (- (cube guess) x)) 0.001))

	(define (average x y z)
		(/ (+ x y z) 3))
	
	(define (improve guess x)
		(average guess guess (/ x (* guess guess))))

	(define (cbrt-iteration guess x)
		(if (good-enough? guess x)
			guess
			(cbrt-iteration (improve guess x) x)))
	
	(cbrt-iteration 1.0 x))

(display "Q1a Cube Root Tests \n")
(display "cube root of 125, expected value 5, actual value: ")
(cbrt 125) ;func is an approximation so works as expected
(display "cube root of 0, expected value 0, actual value: ")
(cbrt 0) ;gotta add an escape case but we can assume that 0 is an invalid input
(display "cube root of -27, expected value -3, actual value: ")
(cbrt -27)
(display "cube root of -1, expected value -1, actual value: ")
(cbrt -1)
(display "cube root of 1, expected value 1, actual value: ")
(cbrt 1)

#| Q1b The newif doesnt work because it will always attempt to evaluate the arguments before it executes the function codes
so you end up in an infinite loop where it is constantly calling another instance of cbrt-iteration |#


#| Q2a Write a recursive procedure (tetra a b) that computes the tetration a↑↑b, where a and b are non-negative integers. |#



(define (tetra a b)
        (cond ((= a 0) 0)
              ((= b 0) 1)
              ((= b 1) a)
              (else (expt a (tetra a (- b 1))))))

(display "Q2a Tetration Tests \n")
(display "2 tetra 4, expected value 65536, actual value: ")
(tetra 2 4)
(display "4 tetra 2, expected value 256, actual value: ")
(tetra 4 2)
(display "3 tetra 3, expected value 7625597484987, actual value: ")
(tetra 3 3)
(display "0 tetra 3, expected value 0, actual value: ")
(tetra 0 3)
(display "1 tetra 3, expected value 1, actual value: ")
(tetra 1 3)
(display "200 tetra 1, expected value 200, actual value: ")
(tetra 200 1)
(display "-2 tetra 3, expected value 0.840896415, actual value: ")
(tetra -2 3)

#| Q2b Rewrite your procedure from part (a) using an iterative process. Call the function (tetra-iter a b). |#

(define (tetra-iter a b)
        (define (tetra-iteration count prod)
          (if(> count (- b 1))
             prod
             (tetra-iteration (+ count 1) (expt a prod))))
         (tetra-iteration 1 a)
  )

(display "Q2b Tetration Tests \n")
(display "2 tetra 4, expected value 65536, actual value: ")
(tetra-iter 2 4)
(display "4 tetra 2, expected value 256, actual value: ")
(tetra-iter 4 2)
(display "3 tetra 3, expected value 7625597484987, actual value: ")
(tetra-iter 3 3)
(display "0 tetra 3, expected value 0, actual value: ")
(tetra-iter 0 3)
(display "1 tetra 3, expected value 1, actual value: ")
(tetra-iter 1 3)
(display "200 tetra 1, expected value 200, actual value: ")
(tetra-iter 200 1)
(display "-2 tetra 3, expected value 0.840896415, actual value: ")
(tetra-iter -2 3)

#| Q3 Write a program called (nuka-cola wallet price caps) that determines how many bottles of nuka-cola you can afford, where,
  wallet is the amount of money you have (integer, >=0)
  price is the cost per bottle (integer, >0)
  caps is how many caps you can trade to get a free bottle (integer, >1) |#

(define (nuka-cola wallet price caps)
        (define (contains a b)
                (/ (- a (modulo a b)) b)) ;function that counts how many of a number (b) can fit in a number (a) by subtracting the modulo division remainder from a, then dividing by b
        (define (bottle-count money cost free)
                (let ((bought-bottles (contains wallet price)))
                  (if (= money 0)
                   0
                   (+  bought-bottles (contains bought-bottles free)))))
        (bottle-count wallet price caps)         
  )

(display "Q3 tests \n")
(display "10 dollars, cost 3 dollars, 3 caps for free bottle, expected 4, actual: ")
(nuka-cola 10 3 3)
(display "15 dollars, cost 3 dollars, 3 caps for free bottle, expected 7, actual: ")
(nuka-cola 15 3 3)
(display "0 dollars, cost 3 dollars, 3 caps for free bottle, expected 0, actual: ")
(nuka-cola 0 3 3)


#| Q4a Write a procedure that computes f by means of a recursive process. Illustrate that your answer is recursive by showing the substitution model for (f 5) in comments below your code.  |#


(define (f n)
    (if (< n 3)
        n
        (+ (* 3 (f (- n 1))) (* 2 (f (- n 2))) (f (- n 3)))))

(f 5)
#|
(f 5)
(+ (* 3 (f (- 5 1))) (* 2 (f (- 5 2))) (f (- 5 3)))
(+ (* 3 (f 4)) (* 2 (f 3)) (f 2))
(+ (* 3 (+ (* 3 (f (- 4 1))) (* 2 (f (- 4 2))) (f (- 4 3)))) (* 2 (+ (* 3 (f (- 3 1))) (* 2 (f (- 3 2))) (f (- 3 3)))) 2)
(+ (* 3 (+ (* 3 (f 3)) (* 2 (f 2)) (f 1))) (* 2 (+ (* 3 (f 2)) (* 2 (f 1)) (f 0))) 2)
(+ (* 3 (+ (* 3 (+ (* 3 (f (- 3 1))) (* 2 (f (- 3 2))) (f (- 3 3)))) (* 2 2) 1)) (* 2 (+ (* 3 2) (* 2 1) 0)) 2)
(+ (* 3 (+ (* 3 (+ (* 3 (f 2)) (* 2 (f 1)) (f 0))) (* 2 2) 1)) (* 2 (+ (* 3 2) (* 2 1) 0)) 2)
(+ (* 3 (+ (* 3 (+ (* 3 2) (* 2 1) 0)) (* 2 2) 1)) (* 2 (+ (* 3 2) (* 2 1) 0)) 2)
(+ (* 3 (+ (* 3 (+ 6 2 0)) 4 1)) (* 2 (+ 6 2 0)) 2)
(+ (* 3 (+ (* 3 8) 4 1)) (* 2 8) 2)
(+ (* 3 (+ 24 4 1)) 16 2)
(+ (* 3 29) 16 2)
(+ 87 16 2)
105
|#

(display "Q4a Expected value 105, actual value: ")
(f 5)


(define (f-iter n)
        (define (f-iteration n1 n2 n3 count)
        (if (= count (- n 2))
             n3
             (f-iteration n2 n3 (+ n1 (* 2 n2) (* 3 n3)) (+ count 1))))
        (if (< n 3)
            n
            (f-iteration 0 1 2 0)))

#|
(f-iter 5)
(f-iter 0 1 2 0)
(f-iter 1 2 8 1)
(f-iter 2 8 29 2)
(f-iter 8 29 105 3)
105
|#

(display "Q4b Expected value 105, actual value: ")
(f-iter 5)

#| Q5a Write a procedure (digits n) that computes the number of digits in the integer n.
 For example, (digits 42) should return 2 and (digits 13579) should return 5.
 You may wish to make use of the built-in floor predicate for truncating decimals to whole numbers.|#

(define (digits n)
        (if (or (= n 1) (= n 0))
            1
            (+ 1 (digits (floor (/ (abs n) 10))))))

(display "Q5a tests \n")
(display "-1231454, expected value 7, actual value: ")
(digits -1231454)
(display "123145489, expected value 9, actual value: ")
(digits 123145489)
(display "0, expected value 1, actual value: ")
(digits 0)

#|Q5b Rewrite your procedure from part (a) using an iterative process. Call the function (digits-iter n). |#

(define (digits-iter n)
        (define (digits-iteration n count)
            (if (or (= n 1) (= n 0))
                (+ count 1)
                (digits-iteration (floor (/ n 10)) (+ 1 count))
            ))
        (digits-iteration (abs n) 0)
  )

(display "Q5b tests \n")
(display "-1231454, expected value 7, actual value: ")
(digits-iter -1231454)
(display "123145489, expected value 9, actual value: ")
(digits-iter 123145489)
(display "0, expected value 1, actual value: ")
(digits-iter 0)

#|Q5c Rewrite either of the previous procedures to create a higher-order procedure called (digits-if pred n).
 This procedure should accept a predicate (boolean procedure) as an additional argument and should count only those digits in n that for which the predicate is true.|#

(define (digits-if pred n)
        (if (pred (modulo n 10))
            (if (or (= n 1) (= n 0))
               1
               (+ 1 (digits-if pred (floor (/ (abs n) 10)))))
            (if (or (= n 1) (= n 0))
               0
               (digits-if pred (floor (/ (abs n) 10))))
 ))
(display "Q5c tests \n")
(display "-1231454 even, expected value 3, actual value: ")
(digits-if even? -1231454)
(display "-1231454 odd, expected value 4, actual value: ")
(digits-if odd? -1231454)
(display "0 even, expected value 1, actual value: ")
(digits-if even? 0)
(display "0 odd, expected value 1, actual value: ")
(digits-if odd? 0)

#| Q5d    Using your solution to the previous problem, fill in the blanks (<???>) below to produce the given output.


	(digits-if (lambda(x)<???>) 21232422) → 5
	(digits-if (lambda(x)<???>) 1889972364) → 6
	(digits-if (lambda(x)<???>) 883689118225) → 3
 |#
(display "(digits-if (lambda(x)<???>) 21232422) → 5 : ")
(digits-if (lambda(x)(if (= x 2) #t #f)) 21232422)

(display "(digits-if (lambda(x)<???>) 1889972364) → 6 : ")
(digits-if (lambda(x)(if (> x 4) #t #f)) 1889972364)

(display "(digits-if (lambda(x)<???>) 883689118225) → 3 : ")
(digits-if (lambda(x)(if (and (> x 2) (< x 7)) #t #f)) 883689118225)


#| Q6  I did not understand at all what you were asking for, how am I supposed to dynamically create infinite defined functions?|#