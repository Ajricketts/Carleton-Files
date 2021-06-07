(define balance 100)
(define (withdraw amount)
    (if (>= balance amount)
        (begin
            (set! balance (- balance amount))
            balance)
        "Insufficient funds"))

(withdraw 40)
(withdraw 40)
(withdraw 40)