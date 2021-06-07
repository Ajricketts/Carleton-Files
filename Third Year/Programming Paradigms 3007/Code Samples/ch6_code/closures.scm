(define z 2)
(define (fun x)
  (lambda (y) (* x y z)))

(define closure1 (fun 3))
(define closure2 (fun 4))

(define r1 (closure1 5))
(define r2 (closure2 5)) 