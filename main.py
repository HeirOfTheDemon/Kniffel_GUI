import login_window
#import number_player_window
#import entry_player_window
#import game_window
#import sqlite3
#import hashlib


login_window.make_login_window()
#number_player_window.make_player_window()
#entry_player_window.make_entry_player_window()
#game_window.make_game_window()


# Wurde für jede*n Spieler*in einmal ausgeführt, um
# die Passwörter zu verschlüsseln
'''connection = sqlite3.connect("./database/user_database.db")
cursor = connection.cursor()

s = hashlib.sha256(b"password123").hexdigest()

cursor.execute(f"UPDATE users SET password ='{s}' WHERE username LIKE 'spieler3';")
connection.commit()
connection.close()'''