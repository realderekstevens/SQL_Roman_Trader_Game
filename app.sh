#!/bin/bash
PSQL="psql -X --username=postgres --dbname=tradergame --tuples-only -c"
echo -e "\n~~~~~ Roman Empire Trader Game ~~~~~\n"
MAIN_MENU() {
	if [[ $1 ]]
	then
		echo -e "\n$1"
	fi
	echo "What would you like to do?"
	echo -e "\n1. Create one person\n2. Delete all the People\n3. Create Tables\n4. Drop All Tables\n0. Exit"
	read MAIN_MENU_SELECTION

	case $MAIN_MENU_SELECTION in
		1) NEW_PERSON ;;
		2) TRUNCATE_TABLE_PEOPLE ;;
		3) CREATE_TABLES ;;
		4) DROP_TABLES ;;
		0) EXIT ;;
		*) MAIN_MENU "Please enter a valid option." ;;
	esac
}

NEW_PERSON(){
for i in {1..3000}
do
	echo "$i / 3000"
	$PSQL "INSERT INTO people(first_name, last_name, location_id) VALUES('Julias', 'Caeser', 1)";
	$PSQL "INSERT INTO people(first_name, last_name, location_id) VALUES('Julias', 'Caeser', 2)";
	$PSQL "INSERT INTO people(first_name, last_name, location_id) VALUES('Julias', 'Caeser', 3)";
	$PSQL "INSERT INTO people(first_name, last_name, location_id) VALUES('Julias', 'Caeser', 4)";
	$PSQL "INSERT INTO people(first_name, last_name, location_id) VALUES('Julias', 'Caeser', 5)";
	$PSQL "INSERT INTO people(first_name, last_name, location_id) VALUES('Julias', 'Caeser', 6)";
	$PSQL "INSERT INTO people(first_name, last_name, location_id) VALUES('Julias', 'Caeser', 7)";
	$PSQL "INSERT INTO people(first_name, last_name, location_id) VALUES('Julias', 'Caeser', 8)";
	$PSQL "INSERT INTO people(first_name, last_name, location_id) VALUES('Julias', 'Caeser', 9)";
	$PSQL "INSERT INTO people(first_name, last_name, location_id) VALUES('Julias', 'Caeser', 10)";
	$PSQL "INSERT INTO people(first_name, last_name, location_id) VALUES('Julias', 'Caeser', 11)";
	clear
done
MAIN_MENU
}

TRUNCATE_TABLE_PEOPLE(){
echo -e "\nDiscarding all the people.\n"
$PSQL "TRUNCATE TABLE people;"
MAIN_MENU
}

DISPLAY_CARDS_IN_DECK(){
$PSQL "SELECT faces.face_name, suits.suit_name FROM ((cards INNER JOIN faces ON cards.face_id = faces.face_id) INNER JOIN suits ON cards.suit_id = suits.suit_id);"
MAIN_MENU
}

DISPLAY_CARD_COUNT(){
$PSQL "SELECT SUM(card_count) FROM cards;"
$PSQL "SELECT SUM(card_count_complex) FROM cards;"
MAIN_MENU
}

CREATE_TABLES(){

$PSQL "CREATE TABLE locations(
	location_id INT GENERATED ALWAYS AS IDENTITY,
   	location_name varchar(255),
   	location_x int,
   	location_y int,
   	population int);"

$PSQL "INSERT INTO locations(
location_name, location_x, location_y) 
VALUES('Rome', 12, 42), 
('Alexandria', 30, 31),
('London', 0, 52),
('Constantinople', 29, 41),
('Antioch', 36, 36),
('Ravenna', 12, 44),
('Mediolanum', 9, 45),
('Ephesus', 27, 38),
('Carthage', 91, 40),
('Lugdunum', 5, 46),
('Thessaloniki', 23, 41);"

$PSQL "CREATE TABLE people(
	person_id INT GENERATED ALWAYS AS IDENTITY,
	first_name VARCHAR(255),
	last_name VARCHAR(255),
	gender_male BOOLEAN DEFAULT 'y',
	employed BOOLEAN DEFAULT 'n',
	employer_id int,
	location_id int,
	title VARCHAR(255) DEFAULT 'Citizen',
	hunger int DEFAULT 50,
	satisfaction int DEFAULT 50,
	politics_x int DEFAULT 50,
	politics_y int DEFAULT 50);"

$PSQL "CREATE TABLE roman_names(
	name_id INT GENERATED ALWAYS AS IDENTITY,
	name VARCHAR(255));"

$PSQL "INSERT INTO roman_names(
name) 
VALUES('Abronius'),
('Abudius'),
('Aburius'),
('Accius'),
('Accoleius'),
('Acerronius'),
('Acilius'),
('Aconius'),
('Actorius'),
('Acutius'),
('Adginnius'),
('Aebutius'),
('Aedinius'),
('Aelius'),
('Aemilius'),
('Aerelius'),
('Afinius'),
('Afranius'),
('Agnanius'),
('Agorius'),
('Albanius'),
('Albatius'),
('Albinius'),
('Albius'),
('Albinovanus'),
('Albucius'),
('Alburius'),
('Alfenus'),
('Alfius'),
('Allectius'),
('Allienus'),
('Amafinius'),
('Amatius'),
('Amblasius');"
MAIN_MENU
}

DROP_TABLES(){
$PSQL "DROP TABLE people;"
$PSQL "DROP TABLE locations;"
$PSQL "DROP TABLE roman_names;"
MAIN_MENU
}

EXIT(){
echo -e "\nThank you for stopping in.\n"
}

MAIN_MENU
