#!/bin/sh

service mysql start
service apache2 start

mysql -u root -e """
drop database exampleDB;
SET PASSWORD = PASSWORD('de3iik17rOC8K3RPWqcKIBeTtCo1UkvUnyC5l5eMiQ75Om5ZWXiqzsaj0f8z');
CREATE USER 'fishies'@'localhost' IDENTIFIED BY 'de3iik17rOC8K3RPWqcKIBeTtCo1UkvUnyC5l5eMiQ75Om5ZWXiqzsaj0f8z';
GRANT SELECT, INSERT, CREATE ON fishshoups.* TO 'fishies'@'localhost';
CREATE DATABASE fishshoups;

USE fishshoups;
CREATE TABLE `fishshoups`.`fish_shop` (`id` INT NOT NULL, `name` VARCHAR(45) NOT NULL, `description` VARCHAR(45) NOT NULL, `image` VARCHAR(45) NOT NULL, `cost` DECIMAL(6,2) NOT NULL, PRIMARY KEY (`id`));
INSERT INTO `fishshoups`.`fish_shop` (`id`, `name`, `description`, `image`, `cost`) VALUES ('1', 'Altum Angel', 'A graceful fish that is relatively aggressive, do not keep with tetras', ' ', '30.00');
INSERT INTO `fishshoups`.`fish_shop` (`id`, `name`, `description`, `image`, `cost`) VALUES ('2', 'Dorado Catfish', 'A beautiful catfish that glimmers in the light eats all the fishes tho.. ', ' ', '128.00');
INSERT INTO `fishshoups`.`fish_shop` (`id`, `name`, `description`, `image`, `cost`) VALUES ('3', 'Bottlenose Catfiiish', 'This fish is a rare fish which is relatively lazy, only active at night', ' ', '68.00');
INSERT INTO `fishshoups`.`fish_shop` (`id`, `name`, `description`, `image`, `cost`) VALUES ('4', 'Schwartzi Cory', 'A wild caught fish that can help you clean up debris and uneaten food, a must buy!', ' ', '30.00');
INSERT INTO `fishshoups`.`fish_shop` (`id`, `name`, `description`, `image`, `cost`) VALUES ('5', 'Diamond Stingray', 'A rare fish that is highly saught after beware the sting!', ' ', '300.00');
INSERT INTO `fishshoups`.`fish_shop` (`id`, `name`, `description`, `image`, `cost`) VALUES ('6', 'Dicrossus filamentosus', 'A nice small fish dont keep with big fishes!', ' ', '10.00');
INSERT INTO `fishshoups`.`fish_shop` (`id`, `name`, `description`, `image`, `cost`) VALUES ('7', 'Fighting Fish', 'Classic fish to keep, This nice specimen is the best we have', ' ', '98.00');
INSERT INTO `fishshoups`.`fish_shop` (`id`, `name`, `description`, `image`, `cost`) VALUES ('8', 'Ghost Knifefish', 'This fish swims gracefully in the tank, a good tank mate for relatively peaceful fish', ' ', '15.00');
INSERT INTO `fishshoups`.`fish_shop` (`id`, `name`, `description`, `image`, `cost`) VALUES ('9', 'Golden Chagoi', 'This is a beautiful fish to have in a pond or aquarium! Great specimen!', ' ', '500.00');
INSERT INTO `fishshoups`.`fish_shop` (`id`, `name`, `description`, `image`, `cost`) VALUES ('10', 'Irwini', 'This catfish is an interesting fish to keep, looks prehistoric.', ' ', '38.00');
INSERT INTO `fishshoups`.`fish_shop` (`id`, `name`, `description`, `image`, `cost`) VALUES ('11', 'L46', 'A rare fish wanted by many,named the king of plecos..', ' ', '100.00');
INSERT INTO `fishshoups`.`fish_shop` (`id`, `name`, `description`, `image`, `cost`) VALUES ('12', 'Pangasius', 'A cute fish that is rather new to the market', ' ', '3.00');
INSERT INTO `fishshoups`.`fish_shop` (`id`, `name`, `description`, `image`, `cost`) VALUES ('13', 'Platy', 'A great fish for beginners! Buy for a new tank', ' ', '2.00');
INSERT INTO `fishshoups`.`fish_shop` (`id`, `name`, `description`, `image`, `cost`) VALUES ('14', 'Red Arrowana', 'The BEST fish to keep if you are rich very nice colors, must buy', ' ', '10288.00');
INSERT INTO `fishshoups`.`fish_shop` (`id`, `name`, `description`, `image`, `cost`) VALUES ('15', 'Freshwater Crayfish', 'New to the market, comes in many colors', ' ', '22');
INSERT INTO `fishshoups`.`fish_shop` (`id`, `name`, `description`, `image`, `cost`) VALUES ('16', 'Spotted Gar', 'Very aggressive and hardy fish, but grows VERY fast, keep if have big tank', ' ', '30.00');
INSERT INTO `fishshoups`.`fish_shop` (`id`, `name`, `description`, `image`, `cost`) VALUES ('17', 'Platinum Alligator Gar', 'Aggressive and hardy species, easy to maintain, just need food', ' ', '160.00');

CREATE TABLE `fishshoups`.`user_details_login` (`user` VARCHAR(45) NOT NULL, `password` VARCHAR(100) NOT NULL, `role` VARCHAR(45) NOT NULL, PRIMARY KEY (`user`));
INSERT INTO fishshoups.user_details_login (`user`, password, `role`) VALUES ('moony', 'amsrISawesome', 'member');
INSERT INTO fishshoups.user_details_login (`user`, password, `role`) VALUES ('potatatoe', 'IamBLUE', 'member');
INSERT INTO fishshoups.user_details_login (`user`, password, `role`) VALUES ('fisheu', 'IswimDEmany', 'admin');
INSERT INTO fishshoups.user_details_login (`user`, password, `role`) VALUES ('Pokey', 'CookiePore', 'member');
INSERT INTO fishshoups.user_details_login (`user`, password, `role`) VALUES ('Merrkat', 'duckOOO', 'member');
INSERT INTO fishshoups.user_details_login (`user`, password, `role`) VALUES ('Darlie', 'secretlyL', 'member');
INSERT INTO fishshoups.user_details_login (`user`, password, `role`) VALUES ('Pusheen', 'immaGREY', 'member');
"""