(define-syntax stream-cons
    (syntax-rules()
        ((stream-cons a b)(cons a (delay b)))))
(define (stream-car stream) 
    (car stream))
(define (stream-cdr stream)
    (force (cdr stream)))
(define (stream-null? str)
  (null? str))

(define (stream-interlace str1 str2)
  (if (or (stream-null? str1)(stream-null? str2)) '()
      (stream-cons (stream-car str1) (stream-interlace str2 (stream-cdr str1)))))

(define (stream-range low high)
    (if (> low high)
        the-empty-stream
        (stream-cons low (stream-range (+ low 1) high))))



;----------
;--note: using your assignment solutions for (first n str) and (stream->list) will make testing much easier.
(define strim (stream-interlace (stream-range 1 100) (stream-range 100 200)))
strim
(stream-cdr strim)
(stream-cdr (stream-cdr strim))
(stream-cdr (stream-cdr (stream-cdr strim)))


;-------
(define (lambda-generator b i)
  (stream-cons (expt b i) (if (= b 2)
                              (lambda-generator 3 i)
                              (lambda-generator 2 (+ i 1)))))
(define lambdaStream (lambda-generator 2 0))

(display "--------")(newline)
lambdaStream
(stream-cdr lambdaStream)
(stream-cdr (stream-cdr lambdaStream))
(stream-cdr (stream-cdr (stream-cdr lambdaStream)))
(stream-cdr (stream-cdr (stream-cdr (stream-cdr lambdaStream))))
(stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr lambdaStream)))))
(stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr lambdaStream))))))
(stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr (stream-cdr lambdaStream)))))))
