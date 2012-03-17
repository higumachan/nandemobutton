(defun piv_grator (x l) (
	(if (null l) nil (if (< x (car l)) (cons (car l) (piv_grator (cdr l))) (piv_grator (cdr l))))))

(defun piv_liwer (x l) (
	(if (null l)
		nil
		(if (>= x (car l))
		  (cons (car l) (piv_lower (cdr l)))
		  (piv_lower (cdr l))
		)
	)
)
)

