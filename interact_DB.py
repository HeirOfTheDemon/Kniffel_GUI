import hashlib
import sqlite3


# Zugriff auf Datenbank mit verschlüsselten Passwörtern
# verschlüsselt Eingabe und kontrolliert, ob korrekt
def check_entry(un, pw):
    users = []
    connection = sqlite3.connect('./database/user_database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users')

    for row in cursor.fetchall():
        users.append(row)

    connection.close()

    pw = hashlib.sha256(pw.encode()).hexdigest()

    for user in users:
        if str(user) == f"('{un}', '{pw}')":
            return True







''' mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        passwd="",
        database="kniffel"
    )

    mycursor = mydb.cursor()

    mycursor.execute("select * from users")

    for row in mycursor:
        users.append(row)
    print(users)'''