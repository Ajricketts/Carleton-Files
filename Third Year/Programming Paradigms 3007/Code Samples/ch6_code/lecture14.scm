(define x 3)
(define (bindEg)
  (define x (+ x 1))
  x)
(define (assignEg)
  (set! x (+ 1 1))
  x)



(define (factorial n)
    (let ((product 1)
          (counter 1))

         (define (iterate)
             (if (> counter n)
                  product
                  (begin
                      (set! product (* counter product))
                      (set! counter (+ counter 1))
                      (iterate))))
         (iterate)))


(define (factorial2 n)
  (define total 1)
  (for-each (lambda(x)(set! total (* total x))) (range 1 n)))


(define (incr x)
  (begin
    (set! x (+ x 1))
    x))

(incr 2)

;(incr 2)
;(begin (set! x (+ 2 1)) 2)   ;we substituted all instances of x->2
;(set! x (+ 2 1)) 2
;2   ;??

