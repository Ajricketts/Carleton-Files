#| Nima Dadar
  100898748 |#

#| Question 1, series of mathematical expressions in scheme |#
(display "Q1 \n")
;a. -1 + 2 + 3 - 4 + -5 + -6, expected output -11, actual output -11
(+ -1 2 3 -4 -5 -6)
;b. 19-9+((12/3 + 4)*(21/7 + 7)), expected output 90, actual output 90
(+(- 19 9) (*(+(/ 21 7) 7) (+(/ 12 3) 4)))
;c. (63/9*(12/4-74/(72+2))+12)/3, expected output 8 2/3 actual output 8 2/3
(/ (+ 12 (* (/ 63 9) (- (/ 12 4) (/ 74 (+ 72 2))))) 3)
;d (200*(5*2))+((301/2.0)-1.6)+(2+20-151), expected output 2019.9, actual output 2019.9
(+ (* 200 5 2) (- (/ 301 2.0) 1.6) (+ 2 20 -151))


#| Question 2 |#
(display "Q2 \n")
;a computes x^3, test cases, positive, negative, decimal, zero and char
(define (cube x) (* x x x))
(cube 3) ;expected output 27, actual 27
(cube -3) ;expected output -27, actual -27
(cube 0) ;expected output 0, actual 0
(cube 1.5) ;expected output 3.375, actual 3.375
;(cube a) ;expected output error, actual "cannot reference an identifier before its definition"

;b. computes f(x) = 3x^3 + 5, given that cube is fully tested only one test is needed for math
(define (f x) (+(* 3 (cube x)) 5))
(f 2) ; expected (3)(2^3) + 5 = 29; actual 29

;c. computes g(x) = 4f(x) + 2x, math test only needed
(define (g x) (+ (* 2 x) (* 4 (f x))))
(g 2) ; expected (4)(29) + (2)(2) = 120, actual 120

;d. computes h(x) = f(x-1) + g(x/2), math test only needed
(define (h x) (+ (f (- x 1)) (g (/ x 2))))
(h 2);expected f(1)= ((3)(1) + 5) = 8, g(1) = (4)(8) + (2)(1) = 34, g(1) + f(1) = 42, actual = 42

#|e. Provide the substitution model using applicative order for (h (* 2 3)).
(h (* 2 3))
(h 6)
(+ (f (- 6 1)) (g (/ 6 2)))
(+ (f (- 6 1)) (g 3))
(+ (f (- 6 1)) (+ (* 2 3) (* 4 (f 3))))
(+ (f (- 6 1)) (+ (* 2 3) (* 4 (+(* 3 (cube 3)) 5))))
(+ (f (- 6 1)) (+ (* 2 3) (* 4 (+(* 3 (* 3 3 3)) 5))))
(+ (f (- 6 1)) (+ (* 2 3) (* 4 (+(* 3 27) 5))))
(+ (f (- 6 1)) (+ (* 2 3) (* 4 (+ 81 5))))
(+ (f (- 6 1)) (+ (* 2 3) (* 4 86)))
(+ (f (- 6 1)) (+ (* 2 3) (* 4 86)))
(+ (f (- 6 1)) (+ 6 344))
(+ (f (- 6 1)) 350)
(+ (f 5) 350)
(+ (+(* 3 (cube 5)) 5) 350)
(+ (+(* 3 (* 5 5 5)) 5) 350)
(+ (+(* 3 125) 5) 350)
(+ (+375 5) 350)
(+ 380 350)
730
|#

#|f. Provide the substitution model using normal order for (h (* 2 3))
(h (* 2 3))
(+ (f (- (* 2 3) 1)) (g (/ (* 2 3) 2)))
(+ (+(* 3 (cube (- (* 2 3) 1))) 5) (+ (* 2 (/ (* 2 3) 2)) (* 4 (f (/ (* 2 3) 2)))))
(+ (+(* 3 (* (- (* 2 3) 1) (- (* 2 3) 1) (- (* 2 3) 1))) 5) (+ (* 2 (/ (* 2 3) 2)) (* 4 (+(* 3 (cube (/ (* 2 3) 2))) 5))))
(+ (+(* 3 (* (- (* 2 3) 1) (- (* 2 3) 1) (- (* 2 3) 1))) 5) (+ (* 2 (/ (* 2 3) 2)) (* 4 (+(* 3 (* (/ (* 2 3) 2) (/ (* 2 3) 2) (/ (* 2 3) 2))) 5))))
(+ (+(* 3 (* (- 6 1) (- 6 1) (- 6 1))) 5) (+ (* 2 (/ 6 2)) (* 4 (+(* 3 (* (/ 6 2) (/ 6 2) (/ 6 2))) 5))))
(+ (+(* 3 (* 5 5 5)) 5) (+ (* 2 (/ 6 2)) (* 4 (+(* 3 (* 3 3 3)) 5))))
(+ (+(* 3 125) 5) (+ (* 2 (/ 6 2)) (* 4 (+(* 3 27) 5))))
(+ (+ 375 5) (+ (* 2 3) (* 4 (+ 81 5))))
(+ 380 (+ 6 (* 4 86)))
(+ 380 (+ 6 344))
(+ 380 350)
730
|#

(h (* 2 3)) ;test for correctness for e and f, outputs 730

#|Question 3|#
(display "Q3a \n")
#|a. Write a procedure called triangle that takes three numbers as arguments representing the three side-lengths of a triangle.
The procedure should classify the triangle and return one of the following strings: "Equilateral" "Isoceles" "Scalene".
NOTE: procedure does not check validity of triangle, any combination of two sides must be greater than the third remaining side|#

(define (triangle x y z)
	(cond   ((and (= x y)(= y z)) "Equilateral")
		((or (= x y)(= y z)(= z x)) "Isoceles")
		(else "Scalene")))

;tests assuming valid input of triangle sides , equilateral output, isoceles output and scalene output, no test for 0, negative or invalid sides because assuming it is a VALID triangle

(triangle 6 6 6) ;expected equilateral, actual equilateral
(triangle 6 6 5) ;expected isoceles, actual Isoceles
(triangle 3 4 5) ;expected scalene, actual scalene

#|b. Write a procedure called convert that takes as arguments: a temperature value (number), and two strings representing the input and output units respectively.
The procedure should support conversions to or from any combination of Celcius ("C"), Fahrenheit ("F"), and Kelvin ("K").
Any other unit argument should result in the return of an error string.|#
(display "Q3b \n")
(define (convert x y z)
	(cond   ((equal? y "C") (cond   ((equal? z "F") (+ (* x (/ 9 5)) 32))
                                   ((equal? z "K") (+ x 273.15))
                                   (else "Error invalid unit of temperature")))
		((equal? y "F") (cond   ((equal? z "C") (* (/ 5 9) (- x 32))) 
                                   ((equal? z "K") (+ 273.15 (* (/ 5 9) (- x 32))))
                                   (else "Error invalid unit of temperature")))
		((equal? y "K") (cond   ((equal? z "F") (+ 32 (* (/ 9 5) (- x 273.15)))) 
                                   ((equal? z "C") (- x 273.15))
                                   (else "Error invalid unit of temperature")))
                (else "Error invalid unit of temperature")))


;tests for b., test each exit of the conditional tree

(convert 32 "C" "F");expected 89.6, actual 89.6
(convert 32 "C" "K");expected 305.15, actual 305.15
(convert 32 "C" "sss");expected error, acutal error
(convert 26 "F" "C"); expected -3.33333, actual -3.33333
(convert 26 "F" "K"); expected 269.816666667; actual 269.816666667
(convert 26 "F" "sss"); expected err
(convert 260 "K" "C"); expected -13.15; actual -13.15
(convert 260 "K" "F"); expected 8.33; actual 8.33
(convert 260 "K" "sss"); expected err

#| Question 4 |#

#|a. Define a procedure between? that takes 3 numbers representing a value (x) and a range (a,b) respectively .
 The procedure should return true if the first argument falls between the remaining two (inclusive), that is if x ∈ [a,b].
Note: the two arguments representing the range can be in either order ([a,b] or [b,a]). |#



(define (between? x y z) (cond   ((and (>= x y) (<= x z)) #t)
		((and (<= x y) (>= x z) #t))
		(else #f)))

;testing all possible cases and formats, upper bound first, lower bound first, equal to upper bound, equal to lower bound
(display "4a. \n")
(between? 7.5 5 10)
(between? 7.5 10 5)
(between? -7.5 10 5) ;should be only false output
(between? 5 10 5)
(between? 10 10 5)
(between? 5 5 10)
(between? 10 5 10)

#|b. Define a procedure called leap? that takes one number as argument and returns true if it represents a valid leap year.
 A leap year is defined as any year that is a multiple of 4. However, any year that is a multiple of 100 is not a leap year, unless the year is a multiple of 400.|#

(define (leap? x) (cond   ((= (modulo x 4) 0) (cond   ((= (modulo x 400) 0) #t)
                                                      ((= (modulo x 100) 0) #f)
                                                      (else #t)))
                          (else #f)))
(display "4b. \n")
;test case for each exit, divisible by 4 and not by 100, not divisible by 4, divisible by 4 but divisible by 100, divisible by 400
(leap? 2016) ;#t
(leap? 2019) ;#f
(leap? 1900) ;#f
(leap? 2000) ;#t

#|c. [3 marks] Define a procedure called days_in_month that takes as arguments two numbers representing a month and a year.
 The procedure should return the number of days in the given month.
Note: the procedure should account for leap years. You may assume valid month and year values are passed in as arguments.|#

(define (days_in_month x y) (cond   ((and (= x 2)(leap? y)) 29)
                                    ((= x 2) 28)
                                    ((or (= x 4) (= x 6) (= x 9) (= x 11)) 30)
                                    (else 31)))

(display "4c. \n")

;tests for question, leap year 29, non leap year 28, 30 days and 31 day month, 
(days_in_month 2 2016)
(days_in_month 2 2019)
(days_in_month 4 2016)
(days_in_month 1 2016)

#|d. Define a procedure called valid_date? that takes three arguments representing the year, month, and day respectively.
 The procedure should return true (#t) if the values are numbers representing a valid date and false (#f) otherwise.|#

(define (valid_date? x y z) (cond   ((or(string? x)(string? y)(string? z)) #f) ;if anything is a string return false
                                    ((< x 0) #f) ; if years are negative not a valid date
                                    ((or(> y 12) (< y 1)) #f) ; checks if month is outside the bounds of actual months
                                    ((or(> z (days_in_month y x))(< z 1)) #f) ;checks if days is not in the amount of days the month has by checking if the date is less than 1 or greater than amount of days in month
                                    (else #t))) ;if it doesnt exit out its true


;test exit on each level and test text requirement
(display "4d. \n")
(valid_date? -1 2 3) ; #f
(valid_date? 2015 13 3) ;#f
(valid_date? 2016 2 32) ;#f
(valid_date? 2016 2 24) ;#t
(valid_date? "2019" "September" "7th") ;#f

#|5 a. What will be the behaviour of this code on an interpreter that uses applicative-order evaluation? Explain why.
Since applicative order evaluates the subexpressions first, you immediately come across a divdie by zero error
as it attempts to evaluate whats inside the arguments to bring the arguments down to primitive types before passing them through the procedure.|#

#|5 b. What behaviour will be observed with an interpreter that uses normal-order evaluation? Explain why.
it'll expand the procedure upon the arguments. so we end up with if(= x 0) then x else y, since x = 0 and y = (/ 3 0) in normal order
it never evaluates y as an expression since (= x 0) returns true, it just returns 0 and never reaches a part code where its required to
evaluate (/ 3 0) thus it never throws the error.
|#

#|6 Observe that Scheme's model of evaluation allows for combinations whose operators are compound expressions.
 Use this observation to describe the behaviour of the following procedure:
(define (foo a b)
		((cond ((> b 0) +)
                       ((= b 0) *)
                       (else /)) a b))

The first thing that happens is b is checked if it is greater than 0, if it is greater than 0 then the operator + is used
(foo a b) becomes (+ a b) given that (> b 0) is true
if its not true it goes to next condition and checks if b = 0, in scheme that is (= b 0)
(foo a b) becomes (* a b) in this case
if b is a negative integer then it goes to default case
(foo a b) becomes (/ a b) in this case.
|#