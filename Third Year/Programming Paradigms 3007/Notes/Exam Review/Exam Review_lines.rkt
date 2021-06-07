(define (make-point x y)
  (cons x y))

(define (x-point point)
  (car point))

(define (y-point point)
  (cdr point))

(define (make-segment p1 p2)
  (cons p1 p2))

(define (start-point segment)
  (car segment))

(define (end-point segment)
  (cdr segment))

(define (mid-point segment)
  (make-point (/ (+ (x-point (start-point segment)) (x-point (end-point segment))) 2)
              (/ (+ (y-point (start-point segment)) (y-point (end-point segment))) 2)))

(define (print-point p)
  (display "(")
  (display (x-point p))
  (display ",")
  (display (y-point p))
  (display ")")
  (newline))

(define p1 (make-point 15 15))
(define p2 (make-point 5 5))
(define s1 (make-segment p1 p2))
(define m1 (mid-point s1))
(print-point m1)