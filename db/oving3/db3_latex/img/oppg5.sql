a)

SELECT sno, sname, status, city 
FROM Supplier 
HAVING status > 15;

b)

SELECT s.sname, s.city 
FROM Supplier s 
JOIN SuppliesPart sp ON s.sno = sp.sno 
JOIN Part p ON sp.pno = p.pno 
WHERE p.pname = 'Screw';

c)

SELECT p.pno, p.pname 
FROM Part p, SuppliesPart sp 
WHERE sp.pno = p.pno 
GROUP BY pname 
HAVING COUNT(*) > 1;

d)

SELECT count(*) AS "AntLev"
FROM Supplier;

e)

SELECT DISTINCT s.city 
FROM Supplier s 
JOIN SuppliesPart sp ON s.sno = sp.sno 
JOIN Part p ON p.pno = sp.pno 
WHERE p.weight > 10.0;

Alternativt: 
SELECT DISTINCT s.city 
FROM Supplier s, Part p, SuppliesPart sp 
WHERE s.sno = sp.sno 
AND p.pno = sp.pno 
AND p.weight > 10.0;

(Disse returnerer et tomt sett, da ingen del i databasen
 veier mer enn 2.0)
(Legger også merke til at det er deler som forsvinner fordi 
 delene ikke eksisterer SuppliesPart, så man kan ikke få ut leverandørby)
 
f)

SELECT s.sname 
FROM Supplier s WHERE s.sno NOT IN(
	SELECT sp.sno 
	FROM SuppliesPart sp, Part p 
	WHERE p.pno = sp.pno 
	AND p.pname = 'Screw')
ORDER BY s.sname ASC;