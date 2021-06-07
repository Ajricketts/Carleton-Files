(define (foo a)
  (define (bar b)
    (+ a b))
  (bar (* a 2)))

(foo 3)
;(foo 3)
;(define (bar b)(+ 3 b))(bar (* 3 2))
;(bar (* 3 2))
;(bar 6)
;(+ 3 6)
;9

(define (g x)(define (f y)(+ x y))(+ (f 3)(f 4)))
(g 5)
;(g 5)
;(define (f y)(+ 5 y))(+ (f 3)(f 4))
;(+ (f 3)(f 4))
;(+ (+ 5 3)(+ 5 4))
;(+ 8 9)
;17

(define (outer x)
  (define (middle y)
    (define (inner z)
      (+ x y z))
    (inner (+ x y)))
  (middle x))

(outer 3) ;=> ?

(let ((a 1)
      (b 2))
  (+ a b))

(define (letExample1 c)
  (let ((a 10)
        (b 32))
    (+ a b c)))

(define (letEx2 x)
  (+ (let ((x 3))
       (+ x (* x 10)))
     x))

;(letEx2 5)
;(+ (let ((x 3))(+ x (* x 10))) 5)
;(+ (+ 3 (* 3 10)) 5)
;(+ (+ 3 30) 5)
;(+ 33 5)
;38

(define (letEx3)
  (let ((x 3)
        (y (+ x 1)))  ;error, x undefined
    (* x y)))
(define (letEx3b)
  (let ((x 3))
    (let ((y (+ x 1)))
      (* x y))))
(define (letEx3c)
  (let* ((x 3)
         (y (+ x 1)))
    (* x y)))


#|(define (usingDef x)
    (if (> x 0)
      (begin (define y 7)
             (+ x y))))
|#

(define (usingLet x)
  (if (> x 0)
      (let ((y 7))
        (+ x y))))