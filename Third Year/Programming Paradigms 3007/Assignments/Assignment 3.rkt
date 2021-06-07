#| Alyxander-Jacob Ricketts
   101084146

|#

(display "##############################################################\n")

#| a.
   Expected input: two functions
   Expected output: a function composed of the two functions given
|#

(display "Question 1a:   ")

(define (compose f g)
  (lambda(x)
       (f (g x))))

(define square (lambda(x)(* x x)))
(define double (lambda(x)(+ x x)))

((compose square double) 3)

(display "Tests for 1a: \n")
((compose square double) 5) ;expected output: 100, output: 100
((compose square double) 7) ;expected output: 196, output: 196
((compose square double) 2) ; expected output: 16, output: 16


#| 1b.
   Expected input: an integer
   Expected output: a true or false value
|#

(display "\n\nQuestion 1b:   ")

(define (divisibleBy n)
  (lambda(x)
    (if (= 0 (modulo x n)) #t #f)))

(define mod3 (divisibleBy 3))
(mod3 7) ;expected output: #f, output: #f
(display "Tests for 1b: \n")
(mod3 9) ;expected output: #t


#| 1c.
   Expected input: a function
   Expected output: a function
|#

(display "\n\nQuestion 1c:   ")

(define (newmap f)
  (define (mapOver f list)
    (if (null? list)
        '()
         (cons (f (car list))
               (mapOver f (cdr list)))))
  (lambda(x)
    (mapOver f x)))

      
(define doubleAll (newmap (lambda(x)(* x 2))))

(doubleAll '(1 2 3 4)) ;expected output: (2 4 6 8), output: (2 4 6 8)
(display "Tests for 1c: \n")
(doubleAll '(10 20 30))  ;expected output: (20 40 60), output: (20 40 60)
(doubleAll '(23 7 9 0))  ;expected output: (46 14 18 0), output: (46 14 18 0)


#| 1d.
   Expected input: a function
   Expected output: a function
|#

(display "\n\nQuestion 1d:   ")

(define (newfilter f)
  (define (filter predicate list)
    (cond ((null? list) '())
          ((predicate (car list))
               (cons (car list)
                     (filter predicate (cdr list))))
          (else (filter predicate (cdr list)))))
  (lambda(x) (filter f x)))

(define filterEvens (newfilter (divisibleBy 2)))

(filterEvens '(10 20 107 3 5 24 37 98 103)) ;expected output: (10 20 24 98), output: (10 20 24 98)

(display "Tests for 1d: \n")
(define filterOdds (newfilter Odd?))
(filterOdds '(10 20 107 3 5 24 37 98 103)) ;expected output: (107 3 5 37 103), output: (107 3 5 37 103)


#| 1e.
   Expected input: a list
   Expected output: an altered list
|#

(display "\n\nQuestion 1e:   ")

(define (range a b)
    (if (= a b) (list a)
        (cons a (range (+ a 1) b))))

(define (myfunc list)
  ((newfilter(divisibleBy 16)) ((newmap square) list)))
(myfunc (range 1 20)) ;expected output: (16 64 144 256 400), output: (16 64 144 256 400)

(display "Tests for 1e: \n")
(myfunc (range 1 12)) ;expected output: (16 64 144), output: (16 64 144)
(myfunc (range 1 30)) ;expected output: (16 64 144 256 400 576 784), output: (16 64 144 256 400 576 784)

(display "\n##############################################################\n")


#| 2a.
   Expected input: a list
   Expected output: an integer (the maximum value)
|#

(display "\nQuestion 2a:   ")

(define (maximum L)
  (if (null? (cdr L))
      (car L)
      (if (> (car L) (car (cdr L)))
          (maximum (cons (car L) (cdr (cdr L))))
          (maximum (cdr L)))))

(display "Tests for 2a: \n")
(maximum '(9 2 4 7 120 12 10 7 18)) ;expected value: 120, ouput: 120
(maximum '(1 95 6 2 75 23 104 4 83 230)) ;expected value: 230, ouput: 230
(maximum '(-1 -95 -30 -1 -102 -16 0 -6 -4 2)) ;expected value: 2, ouput: 2


#| 2b.
   Expected input: a list and an index number
   Expected output: a list
|#

(display "\n\nQuestion 2b:   ")

(define (after L n)
  (if (= n 0)
      L
      (if (= n 1)
          (cdr L)
          (after (cdr L) (- n 1)))))

(after '(a b c d e f g h) 3) ; expected output: (d e f g h), output: (d e f g h)
(display "Tests for 2b: \n")
(after '(a b c d e f g h) 0) ;expected output: (a b c d e f g h), output: (a b c d e f g h)
(after '(-1 -95 -30 -1 -102 -16 0 -6 -4 2) 4) ;expected output: (-102 -16 0 -6 -4 2),  output: (-102 -16 0 -6 -4 2)
(after '(1 95 6 2 75 23 104 4 83 230) 6) ;expected output: (104 4 83 230), output: (104 4 83 230)
(after '(9 2 4 7 120 12 10 7 18) 8) ;expected output: (18), output: (18)


#| 2c.
   Expected input: a list
   Expected output: a list
|#

(display "\n\nQuestion 2c:   ")


(define (after2 L n)
    (if (= n 0)
      '()
      (if (= n 1)
          (cdr L)
          (after2 (cdr L) (- n 1)))))

(define (tails L)
 (define (maxIndex L n)
    (if (equal? (maximum L) (car L)) 
        n
        (maxIndex (cdr L) (+ n 1))))
  
  (if (null? (after2 L (maxIndex L 1)))
             '()
             (begin
               (display (after2 L (maxIndex L 1)))
               (display " ")
               (tails (after2 L (maxIndex L 1))))))

(tails '(3 6 8 9 7 4 8 6 3)) ;expected output: (7 4 8 6 3) (6 3) (3) (), output: (7 4 8 6 3) (6 3) (3) ()
(display "Tests for 2c: \n")
(tails '(4 2 8 7 8 1 2))     ;expected output: (7 8 1 2) (1 2) (), output: (7 8 1 2) (1 2) ()

(tails '(9 2 4 7 120 12 10 7 18 15 9 6 4 5))  ; expected output: (12 10 7 18 15 9 6 4 5) (15 9 6 4 5) (9 6 4 5) (6 4 5) (4 5) (), output: (12 10 7 18 15 9 6 4 5) (15 9 6 4 5) (9 6 4 5) (6 4 5) (4 5) ()


#| 2d:
   Expected input: a list and two integers (those being the start and end indecies)
   Expected output: a sublist
|#

(display "\n\nQuestion 2d:   ")

(define (get-element items i)
    (if (= i 0)
        (car items)
        (get-element (cdr items) (- i 1))))


(define (sublist L start end)
  (if (>= start 1)
      (sublist (cdr L) (- start 1) (- end 1))
      (if (and (> end 0) (not (null? L)))
          (cons (car L) (sublist (cdr L) start (- end 1)))
          '())))
          

(sublist '(0 1 2 3 4 5 6 7 8 9) 3 8) ;expected output: (3 4 5 6 7), output: (3 4 5 6 7)
(display "Tests for 2d: \n")
(sublist '(0 1 2 3 4 5 6 7 8 9) 5 25) ;expected output: (5 6 7 8 9), output: (5 6 7 8 9)
(sublist '(0 1 2 3 4 5) -10 3) ;expected output: (0 1 2), output: (0 1 2)


(display "\n##############################################################\n")

#| 3a.
   Expected input: a list
   Expected output: a filtered list
|#

(display "Question 3a:   ")

(define (tree-filter predicate T)
    (cond ((null? T) '())
          ((list? (car T))
               (cons (tree-filter predicate (car T)) (tree-filter predicate (cdr T))))
          ((predicate (car T)) 
		       (cons (car T) (tree-filter predicate (cdr T))))
          (else (tree-filter predicate (cdr T)))))

(tree-filter even? '(1 (2 3) ((4 5) (6 7)) (((8 (9)))))) ;expected output: ((2) ((4) (6)) (((8 ())))), output: ((2) ((4) (6)) (((8 ()))))

(display "Tests for 3a: \n")
(tree-filter odd? '(1 (2 3) ((4 5) (6 7)) (((8 (9))))))  ;expected output: (1 (3) ((5) (7)) ((((9))))), output: (1 (3) ((5) (7)) ((((9)))))
(tree-filter number? '(1 (2 3) ("random") ((4 5) (6 7)) (((8 (9)))))) ; expected output: (1 (2 3) () ((4 5) (6 7)) (((8 (9))))), output: (1 (2 3) () ((4 5) (6 7)) (((8 (9)))))

#| 3b:
   Expected input: a tree
   Expected output: an integer (the height of the tree)
|#

(display "\n\nQuestion 3b:   ")

(define (height T)
  (cond ((pair? T)
         (+ 1 (max(height (car T)) (height (cdr T)))))
         (else 0)))

(height 'a)                   ;expected value: 0, output: 0
(height '(a))                 ;expected value: 1, output: 1
(height '(a (b) c))           ;expected value: 2, output: 3
(height '(((((a(((b)))))))))  ;expected value: 8, output: 9

; For some reason on the last two test cases it was giving me a count 1 higher than expected and I could not figure out why



#| 3c:
   Expected input: a Tree
   Expected output: a list containing the elements of the tree
|#

(display "\n\nQuestion 3c:   ")

(define (flattenList T)
  (cond ((null? T) '())
        ((list? (car T)) (cons (caar T) (cdar T)))
        ((not (list? (car T))) (cons (car T) (flattenList (cdr T))))
        (else flattenList(cons (car T) (flattenList (cdr T))))))

(flattenList '(1 (2 3) ((4 5 6 (7)))(((8 (9)))))) ;expected output: '(1 2 3 4 5 6 7 8 9), output: ;(1 2 3)

; Could not finish this question all the way in time. 
        




(display "\n##############################################################\n")

#| 4a.
   Expected input: a list
   Expected output: a stream
|#

(display "Question 4a:   ")

(define-syntax stream-cons
    (syntax-rules ()
        ((stream-cons a b)(cons a (delay b)))))
(define (list->stream lis)
  (if (null? lis)
      '()
      (stream-cons (list->stream (car lis)) (list->stream (cdr lis)))))

; Could not finish this question all the way in time.
;(list->stream '(1 2 3 4))



          
