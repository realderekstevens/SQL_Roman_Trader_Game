import sqlite3
import typer
from sqlmodel import Field, Session, SQLModel, create_engine, select
from typing import Optional

app = typer.Typer()
sqlite_file_name = "db.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=True)
connection = sqlite3.connect(sqlite_file_name)
cursor = connection.cursor()

class card(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    rank: str
    value: int
    suit: str
    card_count: int
    card_count_simple: int

class player_hand(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    rank: str
    value: int
    suit: str
    card_count: int
    card_count_simple: int

class player_hand_history(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    rank: str
    value: int
    suit: str
    card_count: int
    card_count_simple: int

class house_hand(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    rank: str
    value: int
    suit: str
    card_count: int
    card_count_simple: int

class house_hand_history(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    rank: str
    value: int
    suit: str
    card_count: int
    card_count_simple: int

class npc1_hand(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    rank: str
    value: int
    suit: str
    card_count: int
    card_count_simple: int

class npc1_hand_history(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    rank: str
    value: int
    suit: str
    card_count: int
    card_count_simple: int

class npc2_hand(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    rank: str
    value: int
    suit: str
    card_count: int
    card_count_simple: int

class npc2_hand_history(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    rank: str
    value: int
    suit: str
    card_count: int
    card_count_simple: int

class npc3_hand(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    rank: str
    value: int
    suit: str
    card_count: int
    card_count_simple: int

class npc3_hand_history(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    rank: str
    value: int
    suit: str
    card_count: int
    card_count_simple: int

class discard_pile(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    rank: str
    value: int
    suit: str
    card_count: int
    card_count_simple: int

@app.command()
def hello(name: str, score: int, display_score: bool = False):
	print(f"Hello {name}")
	if display_score:
		print(f"Your score is {score}")

@app.command()
def goodbye():
	print("Goodbye")

@app.command()
def create_db():
    SQLModel.metadata.create_all(engine)

@app.command()
def create_hearts():
    with Session(engine) as session:
        session.add(card(rank = 2, value = 2, suit = "hearts", card_count = "37", card_count_simple = "1"))
        session.add(card(rank = 3, value = 3, suit = "hearts", card_count = "45", card_count_simple = "1"))
        session.add(card(rank = 4, value = 4, suit = "hearts", card_count = "52", card_count_simple = "1"))
        session.add(card(rank = 5, value = 5, suit = "hearts", card_count = "70", card_count_simple = "1"))
        session.add(card(rank = 6, value = 6, suit = "hearts", card_count = "46", card_count_simple = "1"))
        session.add(card(rank = 7, value = 7, suit = "hearts", card_count = "27", card_count_simple = "0"))
        session.add(card(rank = 8, value = 8, suit = "hearts", card_count = "0", card_count_simple = "0"))
        session.add(card(rank = 9, value = 9, suit = "hearts", card_count = "-17", card_count_simple = "0"))
        session.add(card(rank = 10, value = 10, suit = "hearts", card_count = "-50", card_count_simple = "-1"))
        session.add(card(rank = "J", value = 10, suit = "hearts", card_count = "-50", card_count_simple = "-1"))
        session.add(card(rank = "Q", value = 10, suit = "hearts", card_count = "-50", card_count_simple = "-1"))
        session.add(card(rank = "K", value = 10, suit = "hearts", card_count = "-50", card_count_simple = "-1"))
        session.add(card(rank = "A", value = 11, suit = "hearts", card_count = "-60", card_count_simple = "-1"))
        session.commit()

@app.command()
def create_diamonds():
    with Session(engine) as session:
        session.add(card(rank = 2, value = 2, suit = "diamonds", card_count = "37", card_count_simple = "1"))
        session.add(card(rank = 3, value = 3, suit = "diamonds", card_count = "45", card_count_simple = "1"))
        session.add(card(rank = 4, value = 4, suit = "diamonds", card_count = "52", card_count_simple = "1"))
        session.add(card(rank = 5, value = 5, suit = "diamonds", card_count = "70", card_count_simple = "1"))
        session.add(card(rank = 6, value = 6, suit = "diamonds", card_count = "46", card_count_simple = "1"))
        session.add(card(rank = 7, value = 7, suit = "diamonds", card_count = "27", card_count_simple = "0"))
        session.add(card(rank = 8, value = 8, suit = "diamonds", card_count = "0", card_count_simple = "0"))
        session.add(card(rank = 9, value = 9, suit = "diamonds", card_count = "-17", card_count_simple = "0"))
        session.add(card(rank = 10, value = 10, suit = "diamonds", card_count = "-50", card_count_simple = "-1"))
        session.add(card(rank = "J", value = 10, suit = "diamonds", card_count = "-50", card_count_simple = "-1"))
        session.add(card(rank = "Q", value = 10, suit = "diamonds", card_count = "-50", card_count_simple = "-1"))
        session.add(card(rank = "K", value = 10, suit = "diamonds", card_count = "-50", card_count_simple = "-1"))
        session.add(card(rank = "A", value = 11, suit = "diamonds", card_count = "-60", card_count_simple = "-1"))
        session.commit()

@app.command()
def create_spades():
    with Session(engine) as session:
        session.add(card(rank = 2, value = 2, suit = "spades", card_count = "37", card_count_simple = "1"))
        session.add(card(rank = 3, value = 3, suit = "spades", card_count = "45", card_count_simple = "1"))
        session.add(card(rank = 4, value = 4, suit = "spades", card_count = "52", card_count_simple = "1"))
        session.add(card(rank = 5, value = 5, suit = "spades", card_count = "70", card_count_simple = "1"))
        session.add(card(rank = 6, value = 6, suit = "spades", card_count = "46", card_count_simple = "1"))
        session.add(card(rank = 7, value = 7, suit = "spades", card_count = "27", card_count_simple = "0"))
        session.add(card(rank = 8, value = 8, suit = "spades", card_count = "0", card_count_simple = "0"))
        session.add(card(rank = 9, value = 9, suit = "spades", card_count = "-17", card_count_simple = "0"))
        session.add(card(rank = 10, value = 10, suit = "spades", card_count = "-50", card_count_simple = "-1"))
        session.add(card(rank = "J", value = 10, suit = "spades", card_count = "-50", card_count_simple = "-1"))
        session.add(card(rank = "Q", value = 10, suit = "spades", card_count = "-50", card_count_simple = "-1"))
        session.add(card(rank = "K", value = 10, suit = "spades", card_count = "-50", card_count_simple = "-1"))
        session.add(card(rank = "A", value = 11, suit = "spades", card_count = "-60", card_count_simple = "-1"))
        session.commit()

@app.command()
def create_clubs():
    with Session(engine) as session:
        session.add(card(rank = 2, value = 2, suit = "clubs", card_count = "37", card_count_simple = "1"))
        session.add(card(rank = 3, value = 3, suit = "clubs", card_count = "45", card_count_simple = "1"))
        session.add(card(rank = 4, value = 4, suit = "clubs", card_count = "52", card_count_simple = "1"))
        session.add(card(rank = 5, value = 5, suit = "clubs", card_count = "70", card_count_simple = "1"))
        session.add(card(rank = 6, value = 6, suit = "clubs", card_count = "46", card_count_simple = "1"))
        session.add(card(rank = 7, value = 7, suit = "clubs", card_count = "27", card_count_simple = "0"))
        session.add(card(rank = 8, value = 8, suit = "clubs", card_count = "0", card_count_simple = "0"))
        session.add(card(rank = 9, value = 9, suit = "clubs", card_count = "-17", card_count_simple = "0"))
        session.add(card(rank = 10, value = 10, suit = "clubs", card_count = "-50", card_count_simple = "-1"))
        session.add(card(rank = "J", value = 10, suit = "clubs", card_count = "-50", card_count_simple = "-1"))
        session.add(card(rank = "Q", value = 10, suit = "clubs", card_count = "-50", card_count_simple = "-1"))
        session.add(card(rank = "K", value = 10, suit = "clubs", card_count = "-50", card_count_simple = "-1"))
        session.add(card(rank = "A", value = 11, suit = "clubs", card_count = "-60", card_count_simple = "-1"))
        session.commit()

@app.command()
def drop_db():
    cursor.execute("DROP TABLE IF EXISTS card")
    cursor.execute("DROP TABLE IF EXISTS house_hand")
    cursor.execute("DROP TABLE IF EXISTS player_hand")
    cursor.execute("DROP TABLE IF EXISTS discard_pile")
    cursor.execute("DROP TABLE IF EXISTS npc1_hand")
    cursor.execute("DROP TABLE IF EXISTS npc2_hand")
    cursor.execute("DROP TABLE IF EXISTS npc3_hand")
    connection.commit()

@app.command()
def deal_card_player():
    cursor.execute("INSERT INTO player_hand SELECT * FROM card ORDER BY RANDOM() LIMIT 1")
    rowid = cursor.lastrowid
    #cursor.execute("INSERT INTO player_hand_history SELECT * FROM player_hand WHERE rowid = ?", (rowid,))
    cursor.execute("DELETE FROM card WHERE rowid = ?", (rowid,))
    connection.commit()
    player_value()

@app.command()
def deal_card_house():
    cursor.execute("INSERT INTO house_hand SELECT * FROM card ORDER BY RANDOM() LIMIT 1")
    rowid = cursor.lastrowid
    #cursor.execute("INSERT INTO house_hand_history SELECT * FROM house_hand WHERE rowid = ?", (rowid,))
    cursor.execute("DELETE FROM card WHERE rowid = ?", (rowid,))
    connection.commit()
    house_value()

@app.command()
def deal_card_npc1():
    cursor.execute("INSERT INTO npc1_hand SELECT * FROM card ORDER BY RANDOM() LIMIT 1")
    rowid = cursor.lastrowid
    #cursor.execute("INSERT INTO npc1_hand_history SELECT * FROM npc1_hand WHERE rowid = ?", (rowid,))
    cursor.execute("DELETE FROM card WHERE rowid = ?", (rowid,))
    connection.commit()
    npc1_value()
    
@app.command()
def deal_card_npc2():
    cursor.execute("INSERT INTO npc2_hand SELECT * FROM card ORDER BY RANDOM() LIMIT 1")
    rowid = cursor.lastrowid
    #cursor.execute("INSERT INTO npc2_hand_history SELECT * FROM npc2_hand WHERE rowid = ?", (rowid,))
    cursor.execute("DELETE FROM card WHERE rowid = ?", (rowid,))
    connection.commit()
    npc2_value()
    
@app.command()
def deal_card_npc3():
    cursor.execute("INSERT INTO npc3_hand SELECT * FROM card ORDER BY RANDOM() LIMIT 1")
    rowid = cursor.lastrowid
    #cursor.execute("INSERT INTO npc3_hand_history SELECT * FROM npc3_hand WHERE rowid = ?", (rowid,))
    cursor.execute("DELETE FROM card WHERE rowid = ?", (rowid,))
    connection.commit()
    npc3_value()
    
@app.command()
def card_count():
    cursor.execute("SELECT SUM(card_count) FROM card;")
    print("The card count is:", cursor.fetchone()[0])
    cursor.execute("SELECT SUM(card_count_simple) FROM card;")
    print("The simple card count is:", cursor.fetchone()[0])
    connection.commit()
    
@app.command()
def player_value():
    cursor.execute("SELECT SUM(value) FROM player_hand;")
    value = cursor.fetchone()[0]
    print("You have:", value)
    connection.commit()
    
@app.command()
def house_value():
    cursor.execute("SELECT SUM(value) FROM house_hand;")
    value = cursor.fetchone()[0]
    print("House has:", value)
    connection.commit()
    
@app.command()
def npc1_value():
    cursor.execute("SELECT SUM(value) FROM npc1_hand;")
    value = cursor.fetchone()[0]
    print("NPC1 Has:", value)
    connection.commit()

@app.command()
def npc2_value():
    cursor.execute("SELECT SUM(value) FROM npc2_hand;")
    value = cursor.fetchone()[0]
    print("NPC2 Has:", value)
    connection.commit()

@app.command()
def npc3_value():
    cursor.execute("SELECT SUM(value) FROM npc3_hand;")
    value = cursor.fetchone()[0]
    print("NPC3 Has:", value)
    connection.commit()

def calculate_hand_value(hand):
    value = 0
    has_ace = False
    if rank.isdigit():
        value += int(rank)
    elif rank in ['J', 'Q', 'K']:
        value += 10
    elif rank == 'A':
        has_ace = True
        value =+ 11
        
    if has_ace and value > 21:
        value -= 10
        
    return value

@app.command()
def dealer_logic():
    cursor.execute("SELECT SUM(value) FROM house_hand;")
    value = cursor.fetchone()[0]
    print("House has:", (value))
    while value < 17:
        print("House takes a card")
        deal_card_house()
        cursor.execute("SELECT SUM(value) FROM house_hand;")
        value = cursor.fetchone()[0]
    connection.commit()
    if value > 21:
        print("House busts!")
        print("You win!")
        
@app.command()
def player_logic():
    cursor.execute("SELECT SUM(value) FROM player_hand;")
    value = cursor.fetchone()[0]
    print("Player has:", (value))
    if value < 21:
        response = input("Would you like a card? ")
        if response == "yes":
            deal_card_player()
            connection.commit()
            cursor.execute("SELECT SUM(value) FROM player_hand;")
            value = cursor.fetchone()[0]
            if value > 21:
                print("Player busts!")
                print("You Lose!")
            print("Okay, player stands")
    npc1_logic()
    npc2_logic()
    npc3_logic()

@app.command()
def npc1_logic():
    cursor.execute("SELECT SUM(value) FROM npc1_hand;")
    value = cursor.fetchone()[0]
    print("NPC1 has:", (value))
    while value < 17:
        print("NPC1 takes a card")
        deal_card_npc1()
        cursor.execute("SELECT SUM(value) FROM NPC1_hand;")
        value = cursor.fetchone()[0]
    connection.commit()
    if value > 21:
        print("NPC1 busts!")
        
@app.command()
def npc2_logic():
    cursor.execute("SELECT SUM(value) FROM npc2_hand;")
    value = cursor.fetchone()[0]
    print("NPC2 has:", (value))
    while value < 17:
        print("NPC2 takes a card")
        deal_card_npc2()
        cursor.execute("SELECT SUM(value) FROM NPC2_hand;")
        value = cursor.fetchone()[0]
    connection.commit()
    if value > 21:
        print("NPC2 busts!")
        
@app.command()
def npc3_logic():
    cursor.execute("SELECT SUM(value) FROM npc3_hand;")
    value = cursor.fetchone()[0]
    print("NPC3 has:", (value))
    while value < 17:
        print("NPC3 takes a card")
        deal_card_npc3()
        cursor.execute("SELECT SUM(value) FROM NPC3_hand;")
        value = cursor.fetchone()[0]
    connection.commit()
    if value > 21:
        print("NPC3 busts!")

@app.command()
def new_game():
    drop_db()
    create_db()
    create_hearts()
    create_diamonds()
    create_spades()
    create_clubs()
    deal_round()

@app.command()
def deal_round():
    deal_card_house()
    deal_card_player()
    deal_card_npc1()
    deal_card_npc2()
    deal_card_npc3()
    deal_card_player()
    deal_card_npc1()
    deal_card_npc2()
    deal_card_npc3()
    player_logic()

if __name__ == "__main__":
	app()
