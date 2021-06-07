(define (fac n)
  (cond ((<= n 1) 1)
        (else (* n (fac (- n 1))))))

;(fac 5)
;(* 5 (fac (- 5 1)))
;(* 5 (fac 4))
;(* 5 (* 4 (fac (- 4 1))))
;(* 5 (* 4 (fac 3)))
;(* 5 (* 4 (* 3 (fac 2))))
;(* 5 (* 4 (* 3 (* 2 (fac 1)))))
;(* 5 (* 4 (* 3 (* 2 1))))
;(* 5 (* 4 (* 3 2)))
;(* 5 (* 4 6))
;(* 5 24)
;120

(define (fac-it n)
  (define (helper counter total)
    (if (> counter n)
        total
        (helper (+ counter 1) (* total counter))))
  (helper 1 1))

;(fac-it 5)
;(helper 1 1)
;(helper 2 1)
;(helper 3 2)
;(helper 4 6)
;(helper 5 24)
;(helper 6 120)
;120



(define (recursive)
  (+ 1 (recursive)))

(define (iterative x)
  (iterative (+ x 1)))


;4 * 3 = 3 + 3+ 3+ 3

;iterative
(define (mult1 a b)
  (define (helper counter total)
    (if (= counter 0)
        total
        (helper (- counter 1)(+ total b)))) ;tail-call recursion
  (helper a 0))

;recursive
(define (mult2 a b)
  (if (= a 0) 0
      (+ b (mult2 (- a 1) b))))   ;deferred operations

;gcd
;gcd(a,a) = a
;gcd(a,b) = gcd(a-b,b) if a>b
;gcd(a,b) = gcd(a,b-a) if b>a

(define (gcd a b)
  (cond ((= a b) a)
        ((> a b) (gcd (- a b) b))
        (else (gcd a (- b a)))))

(define (fib n)
  (cond ((= n 0) 0)
        ((= n 1) 1)
        (else (+ (fib (- n 1)) (fib (- n 2))))))

;(fib 5)
;(+ (fib 4)(fib 3))
;(+ (+ (fib 3)(fib 2))(+ (fib 2)(fib 1)))
;...


(define (fibit n)
  (define (iter c fibn-1 fibn-2)
    (if (> c n) fibn-1
        (iter (+ c 1) (+ fibn-1 fibn-2) fibn-1)))
  (iter 2 1 0))

;(fibit 5)
;(iter 2 1 0)
;(iter 3 1 1)
;(iter 4 2 1)
;(iter 5 3 2)
;(iter 6 5 3)
;5

;Problem: Given an amount 'n' and denominations $50, $20, $10, $5
;Write a program that returns the number of permutations of bills that sum to n
;E.g. (atm 20)
;   20, 10 10, 10 5 5,  5 5 5 5  => 4

(define (atm n)
  (define (nextBill bill)
    (cond ((= bill 50) 20)
          ((= bill 20) 10)
          ((= bill 10) 5)
          (else 0)))
 (define (helper amt bill)
   (cond ((= amt 0) 1)
         ((= bill 0) 0)
         ((< amt 0) 0)
         (else (+ (helper (- amt bill) bill)      ;use the bill
                  (helper amt (nextBill bill))))));don't use the bill
  (helper n 50))
