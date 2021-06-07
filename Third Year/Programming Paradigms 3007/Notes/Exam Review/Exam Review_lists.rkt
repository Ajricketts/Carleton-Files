
(define (map procedure list)
  (if (null? list)
      '()
      (cons (procedure (car list))
            (map procedure (cdr list)))))

(define (filter predicate list)
  (cond ((null? list) '())
        ((predicate (car list))
            (cons (car list) (filter predicate (cdr list))))
        (else (filter predicate (cdr list)))))

(define (reduce operator initial list)
  (if (null? list) initial
      (operator (car list)
                (reduce operator initial (cdr list)))))

(define (last L)
  (if (null? (cdr L))
      (car L)
      (last (cdr L))))

(define (leading n L)
  (if (= n 0) '()
      (cons (car L) (leading (- n 1) (cdr L)))))
      
(define (reverse L)
  (if (null? L)
      '()
      (append (reverse (cdr L)) (list (car L)))))

(define (reverse-iter L new)
  (if (null? L)
      new
      (reverse-iter (cdr L) (cons (car L) new))))

(define (tree-map function T)
  (if (null? T) '()
      (if (list? (car T))
          (cons (tree-map function (car T)) (tree-map function (cdr T)))
          (cons (function (car T)) (tree-map function (cdr T))))))

(define (tree-size T)
  (if (null? T) 0
      (if (list? (car T))
          (+ (tree-size (car T)) (tree-size (cdr T)))
          (+ 1 (tree-size (cdr T))))))

      
           


(last '(1 2 3 4 5 6 7))
(leading 4 '(1 2 3 4 5 6 7))                  
(reverse '(1 2 3 4 5 6 7))
(reverse-iter '(1 2 3 4 5 6 7) '())
(tree-map (lambda(x)(* x x)) '(2 (2 3)(4 5 (5 6 7))))
(tree-size '(2 (2 3)(4 5 (5 6 7))))
;(caar '((2 3)(4 5 (5 6 7))))
;(cdr '((2 3)(4 5 (5 6 7))))