3a)
SELECT tittel 
FROM bok;

3b)
SELECT * 
FROM forfatter 
WHERE nasjonalitet = 'Norsk';

3c)
SELECT forlag, navn, telefon
FROM forlag
WHERE adresse = 'Oslo'
ORDER BY forlagnavn;

3e)
SELECT b.tittel, b.utgittår 
FROM bok b, bokforfatter bf, forfatter f 
WHERE b.bokid = bf.bokid 
AND f.forfatterid = bf.forfatterid 
AND f.fornavn = 'Knut' 
AND f.etternavn = 'Hamsun';

3f)
SELECT fornavn, etternavn, fødeår 
FROM forfatter 
WHERE etternavn LIKE "H%";

3i)
SELECT f.fornavn, f.etternavn, 
	(SELECT count(*) 
	 FROM bokforfatter bf 
	 WHERE bf.forfatterid = f.forfatterid) 
AS "AntBok" 
FROM forfatter f 
ORDER BY AntBøker DESC;

3j)
SELECT tittel, utgittår 
FROM bok b 
ORDER BY utgittår ASC LIMIT 1;

3k)
SELECT f.forlagnavn, 
	(SELECT count(*) 
	 FROM bok b 
	 WHERE f.forlagid = b.forlagid) 
AS "AntBok" 
FROM forlag f HAVING antbok > 2;

3l)
SELECT f.forlagnavn 
FROM forlag f 
WHERE f.forlagid NOT IN 
	(SELECT b.forlagid 
	 FROM bok b);
	 
#####################	 
Frivillige oppgaver:
#####################

3d) 
SELECT b.tittel, f.forlagnavn 
FROM bok b, forlag f 
WHERE b.forlagid = f.forlagid;

3g) 
SELECT count(forlagid) AS "AntForlag"
FROM forlag;


3h)
SELECT b.tittel, f.fornavn, f.etternavn, fl.forlagnavn 
FROM bokforfatter bf, bok b, forfatter f, forlag fl 
WHERE bf.bokid = b.bokid 
AND bf.forfatterid = f.forfatterid 
AND b.forlagid = fl.forlagid 
AND f.nasjonalitet = 'Britisk';