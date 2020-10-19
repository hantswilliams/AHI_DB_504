create table book(id int primary key auto_increment, name varchar(50) not null, notes varchar(100));

create view bookview as select id, name from book;
show full tables;

select * from bookview LIMIT 0, 1000;
insert into bookview (id, name) values (2, "War and Peace");
drop table bookview;
