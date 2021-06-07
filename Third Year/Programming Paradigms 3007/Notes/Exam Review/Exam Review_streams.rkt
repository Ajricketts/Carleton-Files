
(define-syntax stream-cons
  (syntax-rules ()
    ((stream-cons a b) (cons a (delay b)))))

(define (stream-car stream)
  (car stream))

(define (stream-cdr stream)
  (force (cdr stream)))

(define (stream-ref n stream)
  (if (= n 0)
      (stream-car stream)
      (stream-ref (- n 1) stream)))

(define (stream-null? str)
  (null? str))


(define (stream-map f stream)
  (if (stream-null? stream) '()
      (if (pair? (stream-car stream))
          (stream-cons (stream-map f (stream-car stream)) (stream-map f (stream-cdr stream)))
          (stream-cons (f (stream-car stream)) (stream-map f (stream-cdr stream))))))

(define (stream-filter predicate stream)
    (cond ((null? stream) '())
          ((predicate (stream-car stream))
              (stream-cons (stream-car stream)
                           (stream-filter predicate 
                                          (stream-cdr stream))))
          (else (stream-filter predicate (stream-cdr stream)))))

(define (integers-starting-from n)
    (stream-cons n (integers-starting-from (+ n 1))))

(define (stream-range low high)
    (if (> low high)
        '()
        (stream-cons low (stream-range (+ low 1) high))))



(define (stream-interlace stream1 stream2)
  (if (or (null? (stream-car stream1)) (null? (stream-car stream2))) '()
      (stream-cons (stream-car stream1) (stream-interlace stream2 (stream-cdr stream1)))))
  

(define (lambda-stream base n)
  (stream-cons (expt base n) (if (= base 2)
                                 (lambda-stream 3 n)
                                 (lambda-stream 2 (+ n 1)))))


#|
(define strim (stream-interlace (stream-range 1 100) (stream-range 100 200)))
strim
(stream-cdr strim)
(stream-cdr (stream-cdr strim))
(stream-cdr (stream-cdr (stream-cdr strim)))
|#

(define lambda (lambda-stream 2 0))
lambda
(stream-cdr lambda)
(stream-cdr (stream-cdr lambda))

#|
(stream-range 1 10)
(stream-cons (stream-cons (stream-cons 1 2) 3) 4)
(stream-map (lambda(x)(* x x)) (stream-cons 2 4))
(stream-filter even? (stream-cons 1 (stream-cons 2 (stream-cons 4 '()))))
|#