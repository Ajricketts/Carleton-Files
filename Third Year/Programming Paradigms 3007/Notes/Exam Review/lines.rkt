(define (print-point p)
  (newline)
  (display "(")
  (display (x-coord p))
  (display ",")
  (display (y-coord p))
  (display ")"))
  
(define (make-point x y)
  (cons x y))

(define (x-coord point)
  (car point))
(define (y-coord point)
  (cdr point))


(define (make-line p1 p2)
  (cons p1 p2))
(define (start-point L)
  (car L))
(define (end-point L)
  (cdr L))
 

(define (avg a b)
  (/ (+ a b) 2))

(define (mid-line L)
  (make-point (avg (x-coord (start-point L)) (x-coord (end-point L)))
              (avg (y-coord (start-point L)) (y-coord (end-point L)))))



;;;;;;;;;;;;;
(define p1 (make-point 0 0))
(define p2 (make-point 4 2))
(define l1 (make-line p1 p2))
(define l2 (make-line (make-point 4 3) (make-point -1 -3)))

(print-point (mid-line l1))
(print-point (mid-line l2))
;;;;;;;;;;;;;;;;;;;;;;;;;;;

