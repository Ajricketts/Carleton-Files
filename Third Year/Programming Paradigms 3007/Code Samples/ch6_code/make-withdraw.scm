(define (make-withdraw balance)
  (lambda (amount)
    (if (>= balance amount)
        (begin
            (set! balance (- balance amount))
            balance)
        "Insufficient funds")))

(define W1 (make-withdraw 100))
(define W2 (make-withdraw 100))

(W1 40)
(W1 40)
(W1 40)
(W2 40)
(W1 20)