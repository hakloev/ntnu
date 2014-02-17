CREATE ASSERTION KREDITTSJEKK
CHECK ( NOT EXIST (
	SELECT k.kundenr, k.navn, k.kredittgrense 
	FROM kunde k, bestilling b, artikkel a 
	WHERE k.kundenr = b.kundenr 
	AND a.artnr = b.artnr 
	GROUP BY k.kundenr 
	HAVING SUM(a.pris * b.kvantum) < k.kredittgrense));