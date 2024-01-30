import sqlite3 

#åben forbindelse til databasen club-database
connection = sqlite3.connect('club-database.db')
#lav cursor object så vi kan navigere i databasen
cursor = connection.cursor()

#vi har brug for tre tabeller

cursor.execute('CREATE TABLE IF NOT EXISTS player (id TEXT, name TEXT, rating INTEGER)')
cursor.execute('CREATE TABLE IF NOT EXISTS match (match_id INTEGER, date TEXT)')
cursor.execute('CREATE TABLE IF NOT EXISTS results (player_id TEXT, match_id INTEGER, score INTEGER)')

#tilføj spiller, kamp, resultat til databasen
def add_player(id, name, rating):
    cursor.execute('INSERT INTO player (id, name, rating) VALUES (?, ?, ?)', (id, name, rating))
    connection.commit()

def add_match(match_id, date):
    cursor.execute('INSERT INTO match (match_id, date) VALUES (?, ?)', (match_id, date))
    connection.commit()

def add_result(player_id, match_id, score):
    cursor.execute('INSERT INTO results (player_id, match_id, score) VALUES (?, ?, ?)', (player_id, match_id, score))
    connection.commit()

#hent spiller, kamp, resultat fra databasen
def get_player(id):
    cursor.execute('SELECT * FROM player WHERE id=?', (id,))
    return cursor.fetchone()

def get_match(match_id):
    cursor.execute('SELECT * FROM match WHERE match_id=?', (match_id,))
    return cursor.fetchone()

def get_result(player_id, match_id):
    cursor.execute('SELECT * FROM results WHERE player_id=? AND match_id=?', (player_id, match_id))
    return cursor.fetchone()

#opdater spillerrating
def update_rating(id, rating):
    cursor.execute('UPDATE player SET rating=? WHERE id=?', (rating, id))
    connection.commit()



#nu skriver vi bare her. database i sqlite og queries, requests via typescript eller flask