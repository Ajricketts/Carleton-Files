#| Alyxander-Jacob Ricketts
   101084146
|#



(define (make-map values)

#| append function

   Expected input: two lists
   Expected output: a list comprised of the other two lists
|#
  (define (append list2)
    (lambda(values)
      (if (null? values)
          list2
          (cons (car values)
                ((append list2) (cdr values))))))

#| Contains function
   Expected input: a key
   Expected output: a boolean indicating whether the key is in the map or not
|#
  (define (contains? k)
    (lambda(values)
    (if (null? values) #f
        (if (null? (caar values)) #f
            (if (equal? (caar values) k) #t
                ((contains? k) (cdr values)))))))

#| Get function
   Expected input: a key
   Expected output: the inputed key and its value pair
|#
  (define (get k)
    (lambda(values)
    (if (null? values) #f
        (if (null? (caar values)) #f
            (if (equal? (caar values) k) (car values)
                ((get k) (cdr values)))))))

#| Empty funciton
   Expected input: 
   Expected output: a boolean indicating where or not the map is empty
|#
  (define (empty?)
    (lambda(values)
      (if (null? values) #t
          (if (null? (car values)) #t #f))))



#| Print funtion
   Expected input: 
   Expected output: The map printed out to the screen in the format ((k1 . v1)(k2 . v2)(k3 . v3)...(kn . vn))
|#
  (define (print)
      (display values)(newline))


#| remove funciton
   Expected input: a key and a map
   Expected output: a map without the key value pair indicated by the given key
|#  

  (define (remove! k)
    (lambda(values)
    (if (null? values) (display "Element not in list, cannot perform remove")
        (if (null? (caar values)) (display "Element not in list, cannot perform remove")
            (if (equal? (caar values) k) (cdr values)
                (cons (car values) ((remove! k) (cdr values))))))))

#| Put! funciton
   Expected input: a key and a value
   Expected output: a map with that key and value pair added to it
|#
  (define (put! k v)
    (if (null? values)
        (set! values ((cons k v) '()))
        (if ((contains? k) values)
            (begin ((remove! k)values)
                   ((append (cons (cons k v) '())) values))
            ((append (cons (cons k v) '())) values))))

  (define (dispatch method)
    (cond ((eq? method 'put!) put!)
          ((eq? method 'contains?) contains?)
          ((eq? method 'remove!) remove!)
          ((eq? method 'get) get)
          ((eq? method 'print) print)
          ((eq? method 'empty?) empty?)
          (else (lambda() (display "Unknown Request: ")
                          (display method)(newline)))))
dispatch)

  
(define map(make-map '(("a" . 1)("b" . 2))))
(display "Put!:  ")
((map 'put!) "c" 3)
(display "Put!:  ")
((map 'put!) "a" 4)
(display "Remove!:  ")
(((map 'remove!) "c")'(("a" . 1)("b" . 2)("c" . 3)))
(display "Contains?:  ")
(((map 'contains?) "c") '((a . 1)(b . 2)("c" . 3)))
(display "get:  ")
(((map 'get) "a") '(("a" . 1)("b" . 2)("c" . 3)))
(display "Print:  ")
((map 'print))
(display "empty?:  ")
(((map 'empty?)) '(("a" . 1)("b" . 2)("c" . 3)))
(display "empty?:  ")
(((map 'empty?)) '())


#| P.O.I I was not able to implement having the map be persistent, therefore the map must be passed in to all the functions |#