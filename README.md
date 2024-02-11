# sql_black_jack
 
chmod +x app.sh

psql -U postgres
CREATE DATABASE trader_game;
\c trader_game
CREATE TABLE commodities;
ALTER TABLE commodities ADD COLUMN commodity_id SERIAL PRIMARY KEY;
ALTER TABLE commodities ADD COLUMN commodity_type varchar(10);
ALTER TABLE commodities ADD COLUMN commodity_manufacturer varchar(10);
ALTER TABLE commodities ADD COLUMN commodity_value integer;
ALTER TABLE commodities ADD COLUMN commodity_amount integer;
ALTER TABLE commodities ADD COLUMN commodity_production_price integer;

CREATE TABLE buisness(
   buisness_id INT GENERATED ALWAYS AS IDENTITY,
   buisness_founded TIME,
   buisness_owner_id INT,
   buisness_type VARCHAR(255),
   buisness_value int,
   buisness_active BOOLEAN)

CREATE TABLE commodities(
   commodity_id INT GENERATED ALWAYS AS IDENTITY,
   commodity_owner_id int,
   commodity_type varchar(255),
   commodity_manufacturer int,
   commodity_value int,
   commodity_amount int,
   PRIMARY KEY(commodity_id),
   CONSTRAINT fk_manufacturer_id
      FOREIGN KEY(commodity_manufacturer_id)
	  REFERENCES buisnesses(buisness_id)
	  ON DELETE CASCADE,
   CONSTRAINT fk_location_id
      FOREIGN KEY(location_id)
	  REFERENCES locations(location_id)
	  ON DELETE CASCADE);

CREATE TABLE people(
   person_id INT GENERATED ALWAYS AS IDENTITY,
   first_name VARCHAR(255),
   last_name VARCHAR(255),
   gender_male BOOLEAN,
   employed BOOLEAN,
   employer_id int,
   location_id int,
   title VARCHAR(255),
   hunger int,
   satisfaction int,
   owns_brand BOOLEAN)
   
CREATE TABLE locations(
   location id INT GENERATED ALWAYS AS IDENTITY,
   location_name varchar(255),
   location_x int,
   location_y int,
   population int)
   
INSERT INTO location(type_name, location_x, location_y) 
VALUES('Rome', 12, 42), 
('Alexandria', 30, 31),
('London', 0, 52),
('Four', 4),
('Five', 5),
('Six', 6),
('Seven', 7),
('Eight', 8),
('Nine', 9),
('Ten', 10),
('Jack', 10),
('Queen', 10),
('King', 10);

#CREATE TABLE card_counts(
#  card_count_id SMALLINT GENERATED ALWAYS AS IDENTITY,
#   card_count_value_simple SMALLINT NOT NULL,
#   card_count_value_complex SMALLINT NOT NULL,
#   PRIMARY KEY(card_count_id),
#   CONSTRAINT fk_type
#      FOREIGN KEY(type_id)
#	  REFERENCES 

CREATE TABLE locations(
   location_id SMALLINT GENERATED ALWAYS AS IDENTITY,
   location_name VARCHAR(255) NOT NULL,
   PRIMARY KEY(location_id));
   
INSERT INTO locations(location_name) 
VALUES('Deck'), ('Player'), ('Dealer_Hidden'), ('Dealer'), ('Discard_Pile');


#INSERT INTO locations(name) VALUES('Deck');
#INSERT INTO locations(name) VALUES('Player');
#INSERT INTO locations(name) VALUES('Dealer_Hidden');
#INSERT INTO locations(name) VALUES('Dealer');
#INSERT INTO locations(name) VALUES('Discard_Pile');

CREATE TABLE suits(
   suit_id SMALLINT GENERATED ALWAYS AS IDENTITY,
   suit_name VARCHAR(255) NOT NULL,
   PRIMARY KEY(suit_id));

INSERT INTO suits(suit_name) 
VALUES('Clubs'), ('Diamonds'), ('Hearts'), ('Spades');

#INSERT INTO suits(suit_name) VALUES ('Clubs');
#INSERT INTO suits(suit_name) VALUES ('Diamonds');
#INSERT INTO suits(suit_name) VALUES ('Hearts');
#INSERT INTO suits(suit_name) VALUES ('Spades');

CREATE TABLE commodities(
   commodity_id INT GENERATED ALWAYS AS IDENTITY,
   type_id SMALLINT,
   suit_id SMALLINT,
   location_id SMALLINT,
   PRIMARY KEY(commodity_id),
   CONSTRAINT fk_type
      FOREIGN KEY(type_id) 
	  REFERENCES types(type_id)
	  ON DELETE CASCADE,
   CONSTRAINT fk_suit
      FOREIGN KEY(suit_id)
	  REFERENCES suits(suit_id)
	  ON DELETE CASCADE,
   CONSTRAINT fk_location
      FOREIGN KEY(location_id)
	  REFERENCES locations(location_id)
	  ON DELETE CASCADE);

ADD_NEW_DECK(){
echo -e "\nAdding new deck.\n"
$PSQL "INSERT INTO commodities(type_id, suit_id, location_id) VALUES(1, 1, 1), (2, 1, 1), (3, 1, 1), (4, 1, 1), (5, 1, 1), (6, 1, 1), (7, 1, 1), (8, 1, 1), (9, 1, 1), (10, 1, 1), (11, 1, 1), (12, 1, 1), (13, 1, 1), (1, 2, 1), (2, 2, 1), (3, 2, 1), (4, 2, 1), (5, 2, 1), (6, 2, 1), (7, 2, 1), (8, 2, 1), (9, 2, 1), (10, 2, 1), (11, 2, 1), (12, 2, 1), (13, 2, 1), (1, 3, 1), (2, 3, 1), (3, 3, 1), (4, 3, 1), (5, 3, 1), (6, 3, 1), (7, 3, 1), (8, 3, 1), (9, 3, 1), (10, 3, 1), (11, 3, 1), (12, 3, 1), (13, 3, 1), (1, 4, 1), (2, 4, 1), (3, 4, 1), (4, 4, 1), (5, 4, 1), (6, 4, 1), (7, 4, 1), (8, 4, 1), (9, 4, 1), (10, 4, 1), (11, 4, 1), (12, 4, 1), (13, 4, 1);"
MAIN_MENU
}

SELECT type_name FROM commodities INNER JOIN types ON commodities.type_id = types.type_id;

SELECT types.type_name, suits.suit_name FROM ((commodities INNER JOIN types ON commodities.type_id = types.type_id) INNER JOIN suits ON commodities.suit_id = suits.suit_id);

SELECT A.*
FROM actors A
INNER JOIN castings C ON C.actorid = A.id
INNER JOIN movies M ON M.id = C.movieid
WHERE M.title = $title

----

ALTER TABLE commodities ADD FOREIGN KEY(suit_id) REFERENCES suits(suit_id);
ALTER TABLE commodities ADD FOREIGN KEY(location_id) REFERENCES locations(location_id);
ALTER TABLE commodities ADD FOREIGN KEY(value_id) REFERENCES values(value_id);

CREATE TABLE locations();
ALTER TABLE locations ADD COLUMN location_id SERIAL PRIMARY KEY;
ALTER TABLE locations ADD COLUMN name varchar(20);
ALTER TABLE locations ADD COLUMN v\dalue integer;

CREATE TABLE scores(
   score_id INT GENERATED ALWAYS AS IDENTITY,
   turn_id INT,
   location_id SMALLINT,
   score int NOT NULL,
   PRIMARY KEY(score_id));
      CONSTRAINT fk_location
      FOREIGN KEY(location_id)
	  REFERENCES locations(location_id)
	  ON DELETE CASCADE);

CREATE TABLE values();
ALTER TABLE values ADD COLUMN value_id SERIAL PRIMARY KEY;
ALTER TABLE values ADD COLUMN value integer;
ALTER TABLE values ADD COLUMN name VARCHAR(20);

INSERT INTO locations(name, value) VALUES('Deck', 0);
INSERT INTO locations(name, value) VALUES('Discard_Pile', 0);
INSERT INTO locations(name, value) VALUES('Dealer', 0);
INSERT INTO locations(name, value) VALUES('Dealer_Hidden', 0);
INSERT INTO locations(name, value) VALUES('Player', 0);

CREATE TABLE suits();
ALTER TABLE suits ADD COLUMN suit_id SERIAL PRIMARY KEY;
ALTER TABLE suits ADD COLUMN name VARCHAR(10);
