(define (make-account balance)   ;super class
    (define (withdraw amount)
        (if (>= balance amount)
            (begin
                (set! balance (- balance amount))
                balance)
            "Insufficient funds"))

    (define (deposit amount)
        (set! balance (+ balance amount))
        balance)

    (define (dispatch method)
        (cond ((eq? method 'withdraw) withdraw)
              ((eq? method 'deposit) deposit)
	      (else (lambda() (display "Unknown Request: ")
			      (display method)(newline)))))

    dispatch)

(define (chequing-acct balance)  ;type of bank-acct that charges $1 per cheque
  (let ((super (make-account 100)))
    (define (write-cheque amt)
      ((super 'withdraw) (+ amt 1)))
    (define (cash-cheque amt)
      ((super 'deposit) (- amt 1)))
    (define (self message)
      (cond ((eq? message 'write-cheque) write-cheque)
            ((eq? message 'cash-cheque) cash-cheque)
            (else (super message))))
    self))

(define acct (chequing-acct 100))
((acct 'write-cheque) 100)
((acct 'write-cheque) 60)
((acct 'withdraw) 39)
