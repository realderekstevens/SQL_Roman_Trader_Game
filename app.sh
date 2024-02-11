#!/bin/bash
PSQL="psql -X --username=postgres --dbname=blackjack --tuples-only -c"
echo -e "\n~~~~~ Blackjack Simulator ~~~~~\n"

MAIN_MENU() {
	if [[ $1 ]]
	then
		echo -e "\n$1"
	fi

	echo "What would you like to do?"
	echo -e "\n1. New Hand\n2. Discard All Cards\n3. Add New Deck\n4. Display Card Count\n5. Format PostgreSQL\n6. Display Cards in Deck\n0. Exit"
	read MAIN_MENU_SELECTION

	case $MAIN_MENU_SELECTION in
		1) NEW_HAND ;;
		2) DISCARD_ALL_CARDS ;;
		3) ADD_NEW_DECK ;;
		4) DISPLAY_CARD_COUNT ;;
		5) FORMAT_POSTGRESQL ;;
		6) DISPLAY_CARDS_IN_DECK ;;
		0) EXIT ;;
		*) MAIN_MENU "Please enter a valid option." ;;
	esac
}

NEW_HAND(){
echo -e "\nThank you for stopping in.\n"
MAIN_MENU
}

DISCARD_ALL_CARDS(){
echo -e "\nDiscarding all cards.\n"
$PSQL "TRUNCATE TABLE cards;"
MAIN_MENU
}


ADD_NEW_DECK(){
$PSQL "INSERT INTO cards(face_id, suit_id, location_id) VALUES(1, 1, 1), (2, 1, 1), (3, 1, 1), (4, 1, 1), (5, 1, 1), (6, 1, 1), (7, 1, 1), (8, 1, 1), (9, 1, 1), (10, 1, 1), (11, 1, 1), (12, 1, 1), (13, 1, 1), (1, 2, 1), (2, 2, 1), (3, 2, 1), (4, 2, 1), (5, 2, 1), (6, 2, 1), (7, 2, 1), (8, 2, 1), (9, 2, 1), (10, 2, 1), (11, 2, 1), (12, 2, 1), (13, 2, 1), (1, 3, 1), (2, 3, 1), (3, 3, 1), (4, 3, 1), (5, 3, 1), (6, 3, 1), (7, 3, 1), (8, 3, 1), (9, 3, 1), (10, 3, 1), (11, 3, 1), (12, 3, 1), (13, 3, 1), (1, 4, 1), (2, 4, 1), (3, 4, 1), (4, 4, 1), (5, 4, 1), (6, 4, 1), (7, 4, 1), (8, 4, 1), (9, 4, 1), (10, 4, 1), (11, 4, 1), (12, 4, 1), (13, 4, 1)";
echo -e "\nAdded new deck.\n"
MAIN_MENU
}

DISPLAY_CARDS_IN_DECK(){
$PSQL "SELECT faces.face_name, suits.suit_name FROM ((cards INNER JOIN faces ON cards.face_id = faces.face_id) INNER JOIN suits ON cards.suit_id = suits.suit_id);"
MAIN_MENU
}

DISPLAY_CARD_COUNT(){
$PSQL "SELECT SUM(card_count) FROM cards;"
$PSQL "SELECT SUM(card_count_complex) FROM cards;"

echo -e "\nThank you for stopping in.\n"
MAIN_MENU
}

FORMAT_POSTGRESQL(){
$PSQL "DROP TABLE IF EXISTS faces CASCADE; DROP TABLE IF EXISTS locations CASCADE; DROP TABLE IF EXISTS suits CASCADE; DROP TABLE IF EXISTS cards CASCADE; DROP TABLE IF EXISTS scores CASCADE;"
$PSQL "CREATE TABLE locations(location_id SMALLINT GENERATED ALWAYS AS IDENTITY, location_name VARCHAR(255) NOT NULL, PRIMARY KEY(location_id));"
$PSQL "CREATE TABLE suits(suit_id SMALLINT GENERATED ALWAYS AS IDENTITY, suit_name VARCHAR(255) NOT NULL, PRIMARY KEY(suit_id));"
$PSQL "CREATE TABLE faces(face_id SMALLINT GENERATED ALWAYS AS IDENTITY, face_name VARCHAR(255) NOT NULL, face_value SMALLINT NOT NULL, PRIMARY KEY(face_id)); 
$PSQL "INSERT INTO faces(face_name, face_value) VALUES('Ace', 1), ('Two', 2), ('Three', 3), ('Four', 4), ('Five', 5), ('Six', 6), ('Seven', 7), ('Eight', 8), ('Nine', 9), ('Ten', 10), ('Jack', 10), ('Queen', 10), ('King', 10);"
$PSQL "CREATE TABLE cards(card_id INT GENERATED ALWAYS AS IDENTITY, face_id SMALLINT, suit_id SMALLINT, location_id SMALLINT, PRIMARY KEY(card_id), CONSTRAINT fk_face FOREIGN KEY(face_id) REFERENCES faces(face_id) ON DELETE CASCADE, CONSTRAINT fk_suit FOREIGN KEY(suit_id) REFERENCES suits(suit_id) ON DELETE CASCADE, CONSTRAINT fk_location FOREIGN KEY(location_id) REFERENCES locations(location_id) ON DELETE CASCADE);"
$PSQL "CREATE TABLE scores(score_id INT GENERATED ALWAYS AS IDENTITY, turn_id INT, location_id SMALLINT, score int NOT NULL, PRIMARY KEY(score_id));"
MAIN_MENU
}

EXIT(){
echo -e "\nThank you for stopping in.\n"
}

MAIN_MENU