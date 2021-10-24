1. Установить postgresql субд из консоли для убунты либо через инсталяционный пакет на винде +

2. Сменить пароль пользователю postgres
alter user postgres with password '12345';

3. Создать базу данных store
 create database store;

4. Созать таблицу products c колонками (id, name, price)
create table products (id serial primary key, 
                       name varchar(50) unique not null, 
                       price integer not null check(price > 0));

5. Создать таблицу orders с колонками (id, product_id, quantity)
create table orders (id serial primary key, 
                     product_id int, 
                     quantity int not null check(quantity >= 1), 
                     constraint fk_products 
                                foreign key(product_id) 
                                references products(id));


6. Заполнить таблицу продуктов записями
insert into products (name, price) values ('iPhone 13', 29899), 
                                          ('iPhone 13mini', 24999), 
                                          ('iPhone 13Pro', 41999), 
                                          ('iPhone 13ProMax', 63999), 
                                          ('OnePlus 9 Pro', 23799), 
                                          ('Samsung Galaxy S20+', 20999), 
                                          ('Samsung Galaxy S20', 14699), 
                                          ('Xiaomi Poco X3 Pro 6', 6799);

7. Заполнить таблицу заказав заказами которые соответствую товарам
insert into orders (product_id, quantity) values ((select id from products where id=1), 12), 
                                                 ((select id from products where id=2), 3), 
                                                 ((select id from products where id=3), 24), 
                                                 ((select id from products where id=4), 18), 
                                                 ((select id from products where id=5), 9), 
                                                 ((select id from products where id=6), 7), 
                                                 ((select id from products where id=7), 7), 
                                                 ((select id from products where id=8), 29);


8. Сделать выборку в которой есть слфедующие колонки (name, price, quantity, total)
select P.name, P.price, O.quantity, P.price*O.quantity as total 
from products as P, orders as O 
where P.id = O.product_id;

