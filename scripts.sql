use crud2

create table articulos (
id_articulo int  primary key,
nombre varchar(50),
precio int,

)

create table inventario (
id_articulo int,
fecha datetime,
stock int

)

create procedure inventarios(
@id int
)
as
begin
select 
            nombre,
            precio,
            stock,
            cast(fecha as date) as fecha_alta
            from articulos a
            inner join inventario b
            on a.id = b.id_articulo
            where a.id = @id
end

insert into articulos (nombre,precio) values (1,'arroz',20)
insert into articulos (nombre,precio) values (2,'harina',20)


select * from articulos
select * from inventario

insert into inventario (id_articulo,fecha,stock) values (10,GETDATE(),50)


select 
nombre,
precio,
stock,
cast(fecha as date) as fecha_alta

from articulos a
inner join inventario b
on a.id = b.id_articulo





exec  inventarios 10

insert into articulos (id, nombre, precio) values (10,'helado',15)