
--
create table logger (
    id int(11) auto_increment primary key,
    started datetime default current_timestamp,
    finished datetime on update current_timestamp,
    records_updated int(11),
    records_created int(11)
);


--
create table product (
    id int(11) auto_increment primary key,
    category_id int(11),
    sku int(11) not null unique,
    name varchar(255),
    img longblob,
    description text,
    price double,
    size varchar(100),
    casing varchar(100),
    alcohol double,
    province varchar(100),
    country varchar(100),
    brewery varchar(100),
    active tinyint(1) default 1,
    date_created datetime default current_timestamp,
    date_modified datetime on update current_timestamp
);
create index idx_name on product (name);
create index idx_date_created on product (date_created);

create view product_view as select id,category_id,sku,name,description,price,size,casing,alcohol,province,country,brewery,active,date_created,date_modified from product;

--
create table product_data (
    id int(11) auto_increment primary key,
    product_id int(11),
    price double,
    sale_price double,
    savings double,
    expiry_date datetime,
    date_created datetime default current_timestamp
);
create index idx_product_id_date_created on product_data (product_id,date_created);


--
create table categories (
    id int(11) auto_increment primary key,
    parent_id int(11),
    category varchar(100)
);
create index idx_category on categories (parent_id);
