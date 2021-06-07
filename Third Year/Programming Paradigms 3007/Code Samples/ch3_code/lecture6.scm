(define (foo x)(+ x 2))
(define (bar y)(y 3))

(bar foo)
;(bar foo)
;(foo 3)
;(+ 3 2)
;5

(define (func x)
  (if (>= x 0) + -))


(define (sum-int a b)
    (if (> a b)
        0
        (+ a  
           (sum-int (+ a 1) b))))

(define (cube x) (* x x x ))

(define (sum-cubes a b)
    (if (> a b)
        0
        (+ (cube a)
           (sum-cubes (+ a 1) b))))

(define (pi-sum a b)
  (define (pi-next a) (+ a 4))
  (define (pi-term a) (/ 1.0 (* a (+ a 2))))
  (if (> a b)
        0
        (+ (pi-term a)
           (pi-sum (pi-next a) b))))

;higher order function
(define (sum a b next term)
  (if (> a b) 0
      (+ (term a)
         (sum (next a) b next term))))

(define (sum-int2 a b)
  (define (inc x)(+ x 1))
  (define (id x) x)
  (sum a b inc id))

(define (sum-cubes2 a b)
  (define (inc x)(+ x 1))
  (define (cube x)(* x x x))
  (sum a b inc cube))

(define (sum-pi a b)
  (define (pi-next a) (+ a 4))
  (define (pi-term a) (/ 1.0 (* a (+ a 2))))
  (sum a b pi-next pi-term))

;sum even numbers from 1 to 100
(define (evenSum1 a b)
  (define (next x)(if (even? x) (+ x 2)(+ x 1)))
  (define (term x) x)
  (if (even? a) (sum a b next term)
      (sum (+ a 1) b next term)))

;(evenSum 1 5)
;(sum (+ 1 1) 5 next term)
;(sum 2 5 next term)
;(+ (term 2)(sum (next a) b next term)))
;(+ 2 (sum 4 5 next term))
;(+ 2 (+ 4 (sum 6 5 next term)))
;(+ 2 (+ 4 0))
;6


(define (evenSum2 a b)
  (define (evenOrNil x)(if (even? x) x 0))
  (define (inc x) (+ x 1))
  (sum a b inc evenOrNil))
(evenSum2 1 100)


(define (safeOp op x y condition)
  (if (condition x y) (op x y)
      (begin (display "Unsafe operation") #f)))

(define (nonzero x y)
  (not (= 0 y)))
(safeOp / 10 0 nonzero)
(safeOp / 10 2 nonzero)

(define (nonnegative x y)
  (<= y x))
(safeOp - 4 5 nonnegative)
(safeOp - 14 5 nonnegative)


(lambda () (+ 3 4))
((lambda()(+ 3 4)))
(lambda (x)(* x 2))
((lambda(x)(* x 2)) 3)
((lambda (x y z)(+ x (* 2 (- y z)))) 5 10 3)
((lambda (x)(* x x)) 3)

((lambda(x y)(+ (* x x)(* y y))) 2 3)

(safeOp / 10 0 (lambda(x y)(not (= y 0))))
(safeOp / 10 2 (lambda(x y)(not (= y 0))))


;equivalent
(define (square x)(* x x))
(define square (lambda(x)(* x x)))

(define (f g) (g 2))


((lambda(x y z)(+ x y(* z z))) 1 2 3)
(define f
  (lambda (x y)
    (* (+ x y) 2)))

((lambda (i j k)(+ (* 3 i)(- j k)))  3 2 1)
(let ((i 3)(j 2)(k 1)) (+ (* 3 i)(- j k)))

(define (letDemo x)
  (let ((a (* x x x))
        (b (* x x)))
    (+ a b)))

(define (lambdaDemo x)
  ((lambda (a b) (+ a b) ) (* x x x)(* x x)))
                  
((lambda (arg)(arg 2 3)) +)
((lambda (arg)(arg 2 3)) *)
((lambda (arg)(arg 2 3)) (lambda (x y)(+ (* 2 x) y)))


((lambda (x y z)(y (* x(+ 3 z)))) 3 (lambda(x)(- x)) 4)

(define (fun x)
  ((lambda (y)(if (< x y) x y)) 2))
(fun 3)

(define (x y z)((lambda( y z)(- y z)) z y))
(x 3 5)

(define (func x)
  (lambda (y) (+ x y)))
(func 3)
((func 3) 2)
