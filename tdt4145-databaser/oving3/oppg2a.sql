create table poststed (
	postnr char(4),
	poststed varchar(30) not null,
	constraint poststed_pk primary key (postnr)
);

create table artikkel (
	artnr integer, 
	navn varchar(30) not null,
	ant integer not null,
	pris integer not null,
	constraint artikkel_pk primary key (artnr)
);

create table kunde (
	kundenr integer,
	navn varchar(30) not null,
	kredittgrense integer,
	postnr char(4) not null,
	constraint kunde_pk primary key (kundenr),
	constraint kunde_fk foreign key (postnr) references poststed(postnr)
		on update cascade
		on delete cascade
);

create table bestilling (
	artnr integer, 
	kundenr integer,
	kvantum integer,
	constraint bestilling_pk primary key (artnr, kundenr),
	constraint bestilling_fk1 foreign key (artnr) references artikkel(artnr)
		on update cascade
		on delete cascade,
	constraint bestilling_fk2 foreign key (kundenr) references kunde(kundenr)
		on update cascade
		on delete cascade
);

-- poststed
insert into poststed values (3145, 'Tjøme');
insert into poststed values (7051, 'Trondheim');
insert into poststed values (0221, 'Oslo');
insert into poststed values (7070, 'Blokksberg');
-- kunde
insert into kunde values (1, 'Håkon', '5000', 3145);		
insert into kunde values (2, 'Truls', '2500', 7051);		
insert into kunde values (3, 'Arne Merete', '10000', 0221);		
insert into kunde values (4, 'Per Beate', '5500', 7070);
-- artikkel		
insert into artikkel values (1, 'Øl', 400, 34);
insert into artikkel values (2, 'Vann', 20, 50);
insert into artikkel values (3, 'Såpe', 45, 10);
insert into artikkel values (4, 'Stressball', 6, 50);
insert into artikkel values (5, 'Partymood', 1000, 5000);
-- bestilling
insert into bestilling values (1, 1, 3);
insert into bestilling values (1, 2, 3);
insert into bestilling values (2, 1, 3);
insert into bestilling values (1, 4, 3);
insert into bestilling values (1, 3, 3);
insert into bestilling values (2, 2, 3);
insert into bestilling values (4, 1, 3);
insert into bestilling values (5, 1, 3);
insert into bestilling values (3, 2, 3);
insert into bestilling values (3, 3, 3);
insert into bestilling values (3, 4, 3);
