(define (foo y)
  ((lambda(x)y)((lambda(y)(* y y)) y)))
(foo 3)

;(foo 3)
;((lambda(x)3) ((lambda(y)(* y y)) 3))
;((lambda(x)3) (* 3 3))
;((lambda(x)3) 9)
;3


(define (multiplyBy x)
  (lambda(y)(* x y)))
(define double (multiplyBy 2))
(define triple (multiplyBy 3))
(double 5)

;(define double (multiplyBy 2))
;(define double (lambda(y)(* 2 y)))  ;free variable is already substituted

;(double 5)
;(* 2 5)
;10

;(define triple (multiplyBy 3))
;(define triple (lambda(y)(* 3 y))


(((lambda(a)(lambda(b c)(if (> (- b c) a) "pizza" "french fries"))) 5) 10 1)


(define (derivative f dx)
  (lambda(x) (/ (- (f (+ x dx))(f x))(-(+ x dx) x))))

(define (f x) (* 2 (* x x x)))
(define f1 (derivative f 0.001))
(define f2 (derivative f1 0.001))

(f1 3)
(f1 17)

;(#%require plot) ;borrowed from racketlang
;(plot (function f -100 100))
;(plot (function f1 -100 100))
;(plot (function f2 -100 100))

(define (printify prefix suffix)
  (lambda (x) (display prefix)(display x)(display suffix)(newline)))

(define canadianize (printify "" ", eh?"))
(define flandersify (printify "" "-a-doodily-oodily"))
(define robotize (printify "beep" "boop"))

(canadianize "hello")
(flandersify "hello")
(robotize "how are you?")


(define  (safeOp2 op condition)
  (lambda (x y) (if (condition x y) (op x y))))

(define safeDiv (safeOp2 / (lambda(x y)(not (= y 0)))))

(safeDiv 10 0)
(safeDiv 10 3)

(define safeSub (safeOp2 - (lambda(x y)(> x y))))
(safeSub 10 2)
(safeSub 2 10)


