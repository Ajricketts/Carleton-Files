(define x 3)
(define y 2)
(define z (lambda (x)(let ((y 3))(+ x y))))
(z 4)

