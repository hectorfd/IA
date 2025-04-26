create database personas_db
use personas_db

create table personas(
id int primary key auto_increment,
nombre varchar(50) null,
apellido varchar(60) null,
edad int null
)
INSERT INTO personas(nombre, apellido, edad) VALUES
('Hector', 'Ferro', 31),
('Juan', 'Gonzales', 35),
('Pedro', 'Rodriguez',25),
('Carmen', 'Diaz', 40)

update personas set apellido='Ramirez'where id=4

delete from personas where id=4

select * from personas
