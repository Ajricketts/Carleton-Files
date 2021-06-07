(define (a x)
  (define (b)
    (set! x 2))   ;what x are we setting?
  (define (c)
    (define x 0)
    (b))
  (c)
  x)
(a 1)


;lexical => 2
;dynamic => 1