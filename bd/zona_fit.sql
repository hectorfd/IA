create database zona_fit_db
use zona_fit_db

create table cliente(
id int primary key auto_increment,
nombre varchar(60) null,
apellido varchar(60) null,
membresia int null,
UNIQUE INDEX (membresia) 
)

insert into cliente(nombre, apellido, membresia) values
('Hector', 'Ferro', 100),
('Jesus', 'de Nazaret', 200),
('Juan', 'Garcia', 300)

select * from cliente