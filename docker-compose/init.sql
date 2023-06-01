CREATE TABLE `delivery` (
  `id` int not null AUTO_INCREMENT,
  `name` varchar(32) not null,
  `result` boolean not null default 0,
  PRIMARY KEY (`id`)
);

insert into delivery(name, result) values('dusdj', 1);