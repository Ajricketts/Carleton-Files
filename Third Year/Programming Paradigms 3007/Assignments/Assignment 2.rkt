#| Alyxander-Jacob Ricketts
   101084146

|#


(display "Question 1a: ")

#|
(x/y2+2y)/3
|#

(define (cbrt x)

        (define (square y) (* y y))
  
        (define (cube y)(* y y y))

	(define (good-enough? guess)
		(< (abs (- (cube guess) x)) 0.001))

	(define (average x y)
		(/ (+ y (* 2 x)) 3))
	
	(define (improve guess)
		(average guess (/ x (square guess))))

	(define (cbrt-iteration guess)
		(if (good-enough? guess)
			guess
			(cbrt-iteration (improve guess))))
	
	(cbrt-iteration 1.0))





(display "\n\nTests for 1a: \n\n")
(display "cbrt 9, Expected value 2.08010..., Output: ")
(cbrt 9)
(display "cbrt -12, Expected value -2.2894..., Output: ")
(cbrt -12)
(display "cbrt 0, Expected value 0, output: ")
(cbrt 0)
(display "cbrt -1, Expected value: 1, output: ")
(cbrt -1)


(display "\nQuestion 1b: ")
#|
(define (cbrt x)

        (define (new-if predicate consequent alternate)
	   (cond (predicate consequent)
			 (else alternate)))
   
        (define (square y) (* y y))
  
        (define (cube y)(* y y y))

	(define (good-enough? guess)
		(< (abs (- (cube guess) x)) 0.001))

	(define (average x y)
		(/ (+ y (* 2 x)) 3))
	
	(define (improve guess)
		(average guess (/ x (square guess))))

	(define (cbrt-iteration guess)
		(new-if ((good-enough? guess)
			(guess))
			cbrt-iteration (improve guess)))
	
	(cbrt-iteration 1.0)) |#

;(cbrt 9)
(display "No, the new version does not work, as it will always attempt to evaluate
the arguments before it executes the function.\n\n")

(display "#############################################################################################\n")
(display "\nQuestion 2a: ")



(define (tetra a b)

       (define (sqaure a) (* a a))

       (cond ((= b 0) 1)
             ;((= b 1) 1)
             ((= a 0) 0) 
             (else (* a (tetra a (- b 1)))))) 
             



(display "\n\n(tetra 2 8) Expected value: 256, Output: ")
(tetra 2 8)
(display "(tetra 4 7) Expected value: 16384, Output: ")
(tetra 4 7)
(display "(tetra -3 8) Expected value: 6561, Output: ")
(tetra -3 8)

(display "\nQuestion 2b: ")




(define (tetra-iter a b)

      (define (tetra-iteration product counter)
            (if (> counter (- b 1))
                product
                (tetra-iteration (* a product) (+ counter 1))))
        (tetra-iteration a 1))




(display "\n\n(tetra-iter 2 8) Expected value: 256, Output: ")
(tetra-iter 2 8)
(display "(tetra-iter 4 7) Expected value: 16384, Output: ")
(tetra 4 7)
(display "(tetra-iter -3 8) Expected value: 6561, Output: ")
(tetra -3 8)

(display "\n############################################################################################\n")
(display "\nQuestion 3: ")



(define (nuka-cola wallet price caps)

      (if (and (integer? wallet) (>= wallet 0) (integer? price)
                             (> price 0) (integer? caps) (> caps 1))
          ( + (floor (/ wallet price)) (floor (/ (floor (/ wallet price)) caps)))
          (display "Please insure wallet and price are integers greater than or equal to 0, and
cap is an integer that is greater than one\n\n")))




(nuka-cola 15 3 3) ; expected value 6, output: 6
(display "\nTests for Question 3: \n\n")
(display "(nuka-cola 25 2 2), expected value 12, output: ")
(nuka-cola 25 2 2)
(display "\n")
(display "(nuka-cola 10 -1 3) Expected value: Error message, Output: ")
(nuka-cola 10 -1 3)
(display "(nuka-cola 10 -1 3) Expected value: Error message, Output: ")
(nuka-cola 10 0 3)
(display "(nuka-cola 10 -1 3) Expected value: Error message, Output: ")
(nuka-cola 10 3 1)


(display "#############################################################################################\n\n")
(display "Question 4a: ")



(define (f n)

      (if (< n 3) n
          (+ (* 3 (f(- n 1))) (* 2 (f(- n 2))) (f(- n 3)))))




(f 5)

(display "Tests for 4a: \n")
(display "(f 15) Expected value: 41422565, ouput: ")
(f 15)
(display "(f 9)  Expected value: 18184, output: ")
(f 9)

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


(display "\nQuestion 4b: ")



(define (f-iter n)
       (define (f-iteration x y z counter)
             (if (= counter (- n 2))
                 z
                 (f-iteration y z (+ x (* 2 y) (* 3 z)) (+ counter 1))))
       (if (< 3 n)
           n
           (f-iteration 0 1 2 0)))

           




#|
(f-iter 5)

(f-iteration 0 1 2 0)
(f-iteration 1 2 8 1)
(f-iterion 2 8 29 2)
(f-iterion 8 29 105 3)
105

|#
  

(f 5)

(display "Tests for 4b: \n")
(display "(f 15) Expected value: 41422565, ouput: ")
(f 15)
(display "(f 9)  Expected value: 18184, output: ")
(f 9)

(display "\n#############################################################################################\n\n")
(display "Question 5a: ")




(define (digits n)

      (if (= n 0) 1
          (+ (floor (/ (log (abs n)) (log 10))) 1)))




(digits 42875)

(display "Tests for Question 5a: \n")
(display "(digits 23)    Expected value: 2, output: ")
(digits 23)
(display "(digits -9302) Expected value: 4, output: ")
(digits -9302)
(display "(digits 0)     Expected value: 1, output: ")
(digits 0)


(display "\nQuestion 5b: ")





(define (digits-iter n)

     (define (digits-iteration counter n)

       (if (<= n 1)
               counter
               (digits-iteration (+ counter 1) (floor (/ n 10)))))

       (if (= n 0)
           1
           (digits-iteration 0 (abs n)))) ; to account for negative numbers





(digits 23) ; expected value 2, output 2

(display "Tests for Question 5b: \n")
(display "(digits-iter 4233728) Expected value: 7, output: ")
(digits-iter 4233728)
(display "(digits-iter -23843)  Expected value: 5, output: ")
(digits-iter -23843)
(display "(digits 0)            Expected value: 1, output: ")
(digits 0)


(display "\nQuestion 5c: ")




(define (digits-if pred n)

   (if (pred (modulo n 10))
             (if (or (= n 1) (= n 0))
                     0
                     (+ 1(digits-if pred (floor (/ (abs n) 10)))))
             (if (or (= n 1) (= n 0))
                     0
                     (digits-if pred (floor (/ (abs n) 10))))))






(display "Tests for Question 5c: \n")
(display "(digits-if even? 32895) Expected value: 2, ouput: ")
(digits-if even? 32895)
(display "(digits-if even? 7345)  Expected value: 1, ouput: ")
(digits-if even? 7345)
(display "(digits-if even? 44361) Expected value: 3, ouput: ")
(digits-if even? 44361)
(display "(digits-if even? 41)    Expected value: 1, ouput: ")
(digits-if even? 41)

(display "\n\nQuestion 5d: \n\n")



(display "Provided Test Cases: \n\n")

(display "(digits-if (lambda(x) (= x 2)) 21232422):  ")
(digits-if (lambda(x) (= x 2)) 21232422)

(display "(digits-if (lambda(x)(>= x 6)) 1889972364):  ")
(digits-if (lambda(x)(>= x 6)) 1889972364)

(display "(digits-if (lambda(x)(if (and (>= x 3) (<= x 6)) #t #f)):  ")
(digits-if (lambda(x)(if (and (>= x 3) (<= x 6)) #t #f)) 883689118225)

(display "\n#############################################################################################\n")
