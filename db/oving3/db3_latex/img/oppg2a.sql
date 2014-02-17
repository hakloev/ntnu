CREATE TABLE poststed (
	postnr char(4),
	poststed varchar(30) not null,
	CONSTRAINT poststed_pk PRIMARY KEY (postnr)
);

CREATE TABLE artikkel (
	artnr integer, 
	navn varchar(30) not null,
	ant integer not null,
	pris integer not null,
	CONSTRAINT artikkel_pk PRIMARY KEY (artnr)
);

CREATE TABLE kunde (
	kundenr integer,
	navn varchar(30) not null,
	kredittgrense integer,
	postnr char(4) not null,
	CONSTRAINT kunde_pk PRIMARY KEY (kundenr),
	CONSTRAINT kunde_fk FOREIGN KEY (postnr) REFERENCES poststed(postnr)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);

CREATE TABLE bestilling (
	artnr integer, 
	kundenr integer,
	kvantum integer not null,
	CONSTRAINT bestilling_pk PRIMARY KEY(artnr, kundenr),
	CONSTRAINT bestilling_fk1 FOREIGN KEY (artnr) REFERENCES artikkel(artnr)
		ON UPDATE CASCADE
		ON DELETE CASCADE,
	CONSTRAINT bestilling_fk2 FOREIGN KEY (kundenr) REFERENCES kunde(kundenr)
		ON UPDATE CASCADE
		ON DELETE CASCADE
);