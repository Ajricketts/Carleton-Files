

(display "QUESTION 1: ") 
;a
(display "a: ")
(+ -1 2 3 -4 -5 -6)

;b
(display "b: ")
(+ (- 19 9)(* (+ (/ 12 3) 4) (+ (/ 21 7) 7)))

;c
(display "c: ")
(/ (+ (* (/ 63 9) (- (/ 12 4) (/ 74 (+ 72 2)))) 12) 3)

;d
(display "d: ")
(+ (* 200 (* 5 2)) (- (/ 301 2.0) 1.6) (- (+ 2 20) 151))


(display "QUESTION 2: \n\n")


#| a.
   Expected input: an integer
   Expected output: an integer (the input given cubed)
|#
(define (cube x) (* x x x))


#| Test Cases
  (cube 5) ;125 
  (cube 9) ;729
|#

#| b.
   Expected input: an integer
   Expected output: an integer
|#
(define (f x) (+ (* 3 (cube x)) 5))



#| Test Cases
  (f 7) ;1034
  (f 3) ;86
|#

#| c.
   Expected input: an integer
   Expected output: an integer
|#
(define (g x) (+ (* 4 (f x)) (* 2 x)))


#| Test Cases
   (g 12) ;20780
   (g 9) ;8786
|#



#| d.
   Expected input: an integer
   Expected output: an integer
|#
(define (h x) (+ (f (- x 1)) (g (/ x 2))))

#|
   Test Cases

  (h 5)
  (h 10)
|#

#| e Applicative order for (h (* 2 3))
   (h (* 2 3))
   (h 6)
   (+ (f (- 6 1)) (g (/ 6 2)))
   (+ (f 5) (g 3))
   (+ (+ (* 3 (cube 5)) 5) (+ (* 4 (f 3)) (* 2 3))
   (+ (+ (* 3 (125)) 5) (+  (* 4 (+ (* 3 (cube 3)) 5)) (* 2 3))
   (+ (+ (* 3 125) 5) (+  (* 4 (+ (* 3 27) 5)) (* 2 3))
   (+ (+ 375 5) (+  (* 4 (+ 81 5)) (* 2 3))
   (+ 380 (+ (* 4 86) (* 2 3))
   (+ 380 (+ 344 6))
   (+ 380 350)
   result: 730
|#
(Display "e: ")
(h (* 2 3)) ;730

#| f Normal Order for (h (* 2 3))

   (h (* 2 3))
   (+ (f (- (* 2 3) 1)) (g (/ (* 2 3) 2)))
   (+ (f (- (* 2 3) 1)) (g (/ (* 2 3) 2)))
   (+ (+ (* 3 (cube (- (* 2 3) 1))) 5) (+ (* 4 (f (/ (* 2 3) 2))) (* 2 (/ (* 2 3) 2)))
   (+ (+ (* 3 (* (- (* 2 3) 1) (- (* 2 3) 1) (- (* 2 3) 1))) 5) (+  (* 4 (+ (* 3 (* (/ (* 2 3) 2) (/ (* 2 3) 2) (/ (* 2 3) 2))) 5)) (* 2 3)))
   (+ (+ (* 3 (* (- 6 1) (- 6 1) (- 6 1))) 5) (+  (* 4 (+ (* 3 (* (/ (* 2 3) 2) (/ (* 2 3) 2) (/ (* 2 3) 2))) 5)) (* 2 3)))
   (+ (+ (* 3 (* 5 5 5) 5) (+  (* 4 (+ (* 3 (* (/ (* 2 3) 2) (/ (* 2 3) 2) (/ (* 2 3) 2))) 5)) (* 2 3)))
   (+ (+ (* 3 125) 5) (+  (* 4 (+ (* 3 (* (/ (* 2 3) 2) (/ (* 2 3) 2) (/ (* 2 3) 2))) 5)) (* 2 3)))
   (+ (+ 375 5) (+  (* 4 (+ (* 3 (* (/ (* 2 3) 2) (/ (* 2 3) 2) (/ (* 2 3) 2))) 5)) (* 2 3)))
   (+ 380 (+  (* 4 (+ (* 3 (* (/ 6 2) (/ 6 2) (/ 6 2))) 5)) (* 2 3)))
   (+ 380 (+  (* 4 (+ (* 3 (* 3 3 3)) 5)) (* 2 3)))
   (+ 380 (+  (* 4 (+ (* 3 27) 5)) (* 2 3)))
   (+ 380 (+  (* 4 (+ 81 5)) (* 2 3)))
   (+ 380 (+  (* 4 86) (* 2 3)))
   (+ 380 (+ 344 (* 2 3)))
   (+ 380 (+ 344 6))
   (+ 380 350)
   result: 730
  

|#

(display "f: ")
(h (* 2 3)) ;730


#|

   Question 3:

|#

#| a.
   Expected input: three same or unique integers
   Expected output: a string identifying what type of triangle would be made given the input side lengths
|#
(display "\nQUESTION 3: \n\n")
(display "a: ")

(define (triangle x y z)
        (cond    ((and (= x y) (= x z)) (display "Equilatiral \n"))
                 ((or (and (not (= x y)) (= x z))
                      (and (not (= x z)) (= y z))
                      (and (not (= y z)) (= x y))) (display "Isocoles \n"))
                 ((and (not (= x y)) (not (= y z)) (not (= x z)) (display "Scalene \n")))))

(triangle 5 5 5)

#| Test Cases

   (triangle 5 5 5)
   (triangle 5 4 5)
   (triangle 5 5 4)
   (triangle 4 5 3)
|#


#| b.

   For helper Functions:
      Expected input: an integer
      Expected output: an integer (Converted)

   For convert:
      Expected input: an integer as the first parameter, and two strings (C, F, K, uppercase or lowercase) denoting whether the degrees inputed is in Celcius, Farinhieght or Kelvins
      Expected output: the converted number
|#

(define (CtoF x) (+ (* x (/ 9 5)) 32))
(define (CtoK x) (+ x 273.15))
(define (FtoC x) (* (- x 32) (/ 5 9)))
(define (FtoK x) (+ (* (- x 32) (/ 5 9)) 273.15))
(define (KtoF x) (+ (* (- x 273.15) (/ 9 5) 32)))
(define (KtoC x) (- x 273.15))
 

(define (convert x y z)
        (cond   ((and (or (equal? y "C") (equal? y "c")) (or (equal? z "F") (equal? z "f")))
                (CtoF x))
                ((and (or (equal? y "C") (equal? y "c")) (or (equal? z "K") (equal? z "k")))
                (CtoK x))
                ((and (or (equal? y "F") (equal? y "f")) (or (equal? z "C") (equal? z "c")))
                (FtoC x))
                ((and (or (equal? y "F") (equal? y "f")) (or (equal? z "K") (equal? z "k")))
                (FtoK x))
                ((and (or (equal? y "K") (equal? y "k")) (or (equal? z "F") (equal? z "f")))
                (KtoF x))
                ((and (or (equal? y "K") (equal? y "k")) (or (equal? z "C") (equal? z "c")))
                (KtoC x))
         )
  )

(display "\nb: ")
(convert 48 "F" "c") ;80/9

#| Test Cases

   (convert 48 "C" "F") 592/5
   (convert 48 "C" "K") 321.15
   (convert 48 "F" "C") 80/9
   (convert 48 "F" "K") 282.03888
   (convert 48 "K" "C") -225.1499
   (convert 48 "K" "F") -12968.64

   or any other uper or lowercase combination

|#


(display "\nQUESTION 4: \n")

#| a.
   Expected input: Three integers, the number you wish to test first, and then the bounds you wish to test it in, in the next two paramaters
   Expected output: A true or false value denoting whether the number provided was inside the range (inclusive)
|#
(define (between? x y z)
        (if (> y z) (<= z x y) (<= y x z)))

(display "\na: ")
(between? 4 3 10) ; #t
;(between? 4 10 3)   #t
;(between? 4 5 10)   #f

#| b.
   Expected input: an integer (a year)
   Expected output: a true or false value denoting whether or not the given year was a leap year or not
|#
(define (leap? x)
        (cond   ((and (= 0 (modulo x 4)) (not (= 0 (modulo x 100)))))
                ((and (= 0 (modulo x 4)) (= 0 (modulo x 400))))
                (else (and (= 0 (modulo x 100)) (not (= 0 (modulo x 400))) #f))))                

(display "\nb: ")
(leap? 2016) ; #t
;(leap? 2017)  #f
;(leap? 2000)  #t
;(leap? 1900)  #f

#| c.
   Expected input: Two integers (A month and a year)
   Expected output: an integer (The number of days in that month)
|#
(define (days_in_month month year)
        (cond    ((or (= month 1) (= month 3) (= month 5) (= month 7) (= month 8) (= month 10) (= month 12)) 31)
                 ((or (= month 4) (= month 6) (= month 9) (= month 11)) 30)
                 ((and (leap? year) (= month 2) 29))
                 (else 28))) 

(display "\nc: ")
(days_in_month 3 2013) ;31
(days_in_month 9 2017) ;30
(days_in_month 2 2016) ;29
(days_in_month 2 2017) ;28
(days_in_month 4 2016) ;30

(display "\nd: \n\n")

#| b.
   Expected input: Three integers, the year month and day in that order
   Expected output: A true or false value denoting whether the given date was a valid date
|#
(define (valid_date? year month day)
        (cond    ((or (string? year) (string? month) (string? day)) #f)
                 ((or (< year 0) (< day 0)) #f)
                 ((or (> month 12) (< month 1)) #f)
                 ((or (> day (days_in_month month year)) (< day 1)) #f)
                 (else #t)))
                     
(valid_date? 2014 10 3) ; #t
(valid_date? 2016 2 29) ; #t
(valid_date? -3000 14 87) ; #f
(valid_date? "2019" "September" "7th") ; #f


(display "\nQUESTION 5: \n\n")
(display "a:  Given that applicative order evalutes expressions before they are passed as arguments, an interpreter that usses applicative order will display an error as it will try to\n
    evaluate (/ 3 0) which will give a divide by zero error. If this error is shown you know your interpretor is ussing applicative order evaluation.\n\n")

(display "b:  If your interpreter uses normal order evaluation then it pass both 0 and (/ 3 0) as arguments in test as x and y. This will then lead to the evaluation\n
    of (if (= x 0)) which will return true and the error will never be reached.")


(display "\n\nQUESTION 6: \n\n")

(display "Given the following observation: \n\n")
(display "(define (foo a b)
		((cond ((> b 0) +)
                       ((= b 0) *)
                       (else /)) a b))\n\n")
(display "What will happen is if b is > then zero for example, then the operator returned is +. In this case, the experession will turn in to (+ a b) and it will evaluate.")
(display "The same goes fo rthe other two conditions, if (= b 0) is true then the operator returned is * and then the resulting expression will be (* a b), and if neither of those are true\n
(b is a negative integer) then the operator returned will be / and the resulting expression will be (/ a b).")
  