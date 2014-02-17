CREATE VIEW DEPTSUMMARY(PNAME, DEPTNUM, TOTEMP, TOTHOURS)
AS SELECT p.pname, p.dnum, count(*), sum(w.hours)
	FROM project p, works_on w
	WHERE p.pnumber = w.pno
	GROUP BY p.pnumber