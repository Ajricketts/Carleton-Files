(+ 1 2)
(display "Hello scheme!")

; This is an end of line comment

#| This is a
multiline
comment |#

(+ (* (+ 1 2)
      (+ (* 2 4)
         (+ 3 5)))
   (+ (- 10 7) 6))

;7-4*10+12
(* (- 7 4)(+ 10 12))  ;backwards
(+(- 7 (* 4 10)) 12)

;6/3+9*2+(-7)+(3+4*2)
;(6/3)+(9*2)+(-7)+(3+4*2)

(+ (/ 6 3) (* 9 2)(- 7) (+ 3 (* 4 2)))

(* (+ 2 (* 4 6))(+ 3 5 7))
;eval (* (+ 2 (* 4 6))(+ 3 5 7)) => 390
;   eval *  => #<procedure:*>
;   eval (+ 2 (* 4 6)) => 26
;      eval + => #<procedure:+>
;      eval 2 => 2
;      eval (* 4 6) => 24
;          eval * => #<procedure:*>
;          eval 4 => 4
;          eval 6 => 6
;          apply * to 4 6 => 24
;      apply + to 2 24 => 26
;   eval (+ 3 5 7) => 15
;      eval + => #<procedure:+>
;      eval 3 => 3
;      eval 5 => 5
;      eval 7 => 7
;      apply + to 3 5 7 => 15
;   apply * to 26 15 => 390

;(+ (* 3 2)(/ 6 2)(* 6 3)(- 6 3))
;(+ 6 3 18 3)

(display (+ 3 2))(newline)


(define x 7)
x

(define pi 3.14159265358)
(define r 10)

(define circumference (* 2 pi r))

(define height 10)
(define areaCylinder ( + (* circumference height)(* 2 pi (* r r))))

(define areaCylinder (+ (* (* 3.14159265358 10) 10) (* 2 (/ 22 7) (* 10 10))))

(define a "hello")
(define b "world")
(display a)
(display b)
(newline)
;(< a b)  ;dynamic type error


;procedural abstraction

(define (square x)(* x x))
(square 3)
(square (+ 3 4))
(square (square 5))
square

(define (s-o-s x y) (+ (square x)(square y)))

(s-o-s 3 4)

(define (pretty-sum a b)
  (display a)(display " + ")(display b)
  (newline)(display " = ")
  (+ a b))

(define (myfunc a)
  (+ a 1)
  (* a 2)
  (- a a))