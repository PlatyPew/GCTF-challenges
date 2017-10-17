#! /bin/sh
##
# Prepare database and start
mysql_install_db
mysqld --user=root &

# Start webserver
httpd &

# Install database
sleep 10
mysql -u root -e """
SET PASSWORD = PASSWORD('de3iik17rOC8K3RPWqcKIBeTtCo1UkvUnyC5l5eMiQ75Om5ZWXiqzsaj0f8z');
CREATE USER 'fishies'@'localhost' IDENTIFIED BY 'de3iik17rOC8K3RPWqcKIBeTtCo1UkvUnyC5l5eMiQ75Om5ZWXiqzsaj0f8z';
GRANT SELECT, INSERT, CREATE ON fishshoups.* TO 'fishies'@'localhost';
CREATE DATABASE fishshoups;

USE fishshoups;
CREATE TABLE fishshoups.fish_shop (id INT NOT NULL, name VARCHAR(45) NOT NULL, description VARCHAR(200) NOT NULL, image VARCHAR(45) NOT NULL, cost DECIMAL(6,2) NOT NULL, PRIMARY KEY (id));
INSERT INTO fishshoups.fish_shop VALUES ('1', 'Altum Angel', 'A graceful fish that is relatively aggressive, do not keep with tetras', 'image/altum-min.jpg', '30.00');
INSERT INTO fishshoups.fish_shop VALUES ('2', 'Dorado Catfish', 'A beautiful catfish that glimmers in the light eats all the fishes tho.. ', 'image/bestfish-min.jpg', '128.00');
INSERT INTO fishshoups.fish_shop VALUES ('3', 'Bottlenose Catfiiish', 'This fish is a rare fish which is relatively lazy, only active at night', 'image/bottley-min.jpg', '68.00');
INSERT INTO fishshoups.fish_shop VALUES ('4', 'Schwartzi Cory', 'A wild caught fish that can help you clean up debris and uneaten food, a must buy!', 'image/corygood-min.jpg', '30.00');
INSERT INTO fishshoups.fish_shop VALUES ('5', 'Diamond Stingray', 'A rare fish that is highly saught after beware the sting!', 'image/diamond_sting-min.jpg', '300.00');
INSERT INTO fishshoups.fish_shop VALUES ('6', 'Dicrossus filamentosus', 'A nice small fish dont keep with big fishes!', 'image/fastswim-min.jpg', '10.00');
INSERT INTO fishshoups.fish_shop VALUES ('7', 'Fighting Fish', 'Classic fish to keep, This nice specimen is the best we have', 'image/fighting-min.jpg', '98.00');
INSERT INTO fishshoups.fish_shop VALUES ('8', 'Ghost Knifefish', 'This fish swims gracefully in the tank, a good tank mate for relatively peaceful fish', 'image/ghost-min.jpg', '15.00');
INSERT INTO fishshoups.fish_shop VALUES ('9', 'Golden Chagoi', 'This is a beautiful fish to have in a pond or aquarium! Great specimen!', 'image/golden chagoi-min.jpg', '500.00');
INSERT INTO fishshoups.fish_shop VALUES ('10', 'Irwini', 'This catfish is an interesting fish to keep, looks prehistoric.', 'image/irwini-min.jpg', '38.00');
INSERT INTO fishshoups.fish_shop VALUES ('11', 'L46', 'A rare fish wanted by many,named the king of plecos..', 'image/l46-min.jpg', '100.00');
INSERT INTO fishshoups.fish_shop VALUES ('12', 'Pangasius', 'A cute fish that is rather new to the market', 'image/Pangasius_larnaudii-min.jpg', '3.00');
INSERT INTO fishshoups.fish_shop VALUES ('13', 'Platy', 'A great fish for beginners! Buy for a new tank', 'image/platy-min.jpg', '2.00');
INSERT INTO fishshoups.fish_shop VALUES ('14', 'Red Arrowana', 'The BEST fish to keep if you are rich very nice colors, must buy', 'image/red_arrow-min.jpg', '10288.00');
INSERT INTO fishshoups.fish_shop VALUES ('15', 'Freshwater Crayfish', 'New to the market, comes in many colors', 'image/RIP_LOBBY-min.jpg', '22');
INSERT INTO fishshoups.fish_shop VALUES ('16', 'Spotted Gar', 'Very aggressive and hardy fish, but grows VERY fast, keep if have big tank', 'image/spotted_gar-min.jpg', '30.00');
INSERT INTO fishshoups.fish_shop VALUES ('17', 'Platinum Alligator Gar', 'Aggressive and hardy species, easy to maintain, just need food', 'image/white_gar-min.jpg', '160.00');
INSERT INTO fishshoups.fish_shop VALUES ('18', 'Poecilia Reticulata', 'A guppy, also known as rainbow fish. It\'s colourful and are great pets. LFlare approves', 'image/sexy_pose.jpg', '3.00');


CREATE TABLE fishshoups.user_details_login (user VARCHAR(45) NOT NULL, password VARCHAR(45) NOT NULL, role VARCHAR(45) NOT NULL, PRIMARY KEY (user));
INSERT INTO fishshoups.user_details_login VALUES ('Chocolateee', 'Isbad', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('BuyMe', 'Gummies', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('Hello', 'Humanszzz', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('IAm', 'DeAwesaomesr', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('Autismist', 'IsNotMe', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('IMiss', 'MyDramas', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('SaveMe', 'frmMisery', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('Look', 'Carefully', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('DOYOUEVERFEL', 'likeaplasticbag', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('DES', 'IsDes', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('Idk', 'WhatToNamealr', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('Flamingo', 'Red', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('HowManuy', 'Shrimps', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('Doyou', 'Havetoeat', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('Until', 'youMAke', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('YOUR', 'SkinTurn pinkkkk', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('EAtTo', 'Much', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('And ', 'Youwill', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('GetSick', 'ShrimpsAre', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('Pretty', 'Rich', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('Katy', 'Perri', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('ISpelledDAT', 'WRONGyasik', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('Help', 'IMLAZY', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('toTYPOREO', 'TIREDYO', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('YAY', 'MEiisNOGIVEUP', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('Determination', 'GOINGSTRONK', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('AMDEDEDED', 'handsCRYING', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('Afewmoreeee', 'ToGO', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('RESILIENCE', 'ISkey', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('GivingUP', 'ISbad', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('FISH', 'isGOOD', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('CRI', 'DONING', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('Bob', 'Bob', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('moony', 'amsrISawesome', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('potatatoe', 'IamBLUE', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('fisheu', 'IswimDEmany', 'admin');
INSERT INTO fishshoups.user_details_login VALUES ('Pokey', 'CookiePore', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('Merrkat', 'duckOOO', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('Darlie', 'secretlyL', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('Pusheen', 'immaGREY', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('Manny', 'Barley', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('Bart', 'Karlet', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('Chocolate', 'Sucks', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('Gummies', 'Dabestestestest', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('Duckyyyyy', 'Quack', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('Matamata', 'Pourise', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('Llala', 'sdfas', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('sfdsf', 'trbyrty', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('cdsdfs', 'sefce', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('fsdf', 'fsdcfew', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('fwec', 'uyne', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('xwxwz', 'iuyt', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('asdfg', 'ghjk', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('dsf', 'fds', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('IMLAZY', 'Totypeeeeeeee', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('ButOwell', 'fsdf', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('fsedf', 'cewxee', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('poihhg', 'vvfer', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('qrvrgefw', 'lkjhg', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('tbtbt', 'bbrrwef', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('poli', 'sfdsdf', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('ecsdc', 'dsfsdf', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('axrgght', 'hybj', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('ecwefc', 'efcefecfer', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('ercwec', 'dfcsfce', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('vetere', 'fewfce', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('BYE', 'BYWW', 'member');
INSERT INTO fishshoups.user_details_login VALUES ('BYEE', 'BYEEEEEEEE', 'member');

"""

# Never exit
tail -f /dev/null
