import tkinter as tk
import game_window
from class_player import Player

player_names = []
list_player = []
# Öffnet das Spielfenster
def open_game(firstwindow):
    firstwindow.destroy()
    game_window.make_game_window()


# Populiert die eingetragenen SpielerInnen-Namen
# in eine Liste
def retrieve_player_name(text):
    player_name = text.get("1.0", "end-1c")
    player_names.append(player_name)

# Erstellt für die Einträge die im Spiel gemacht werden jeweils ein
# neues SpielerInnen-Objekt
def create_player_objects():
    global list_player
    list_player = []
    for player_name in player_names:
        player = Player(player_name)
        list_player.append(player)


# Macht ein Fenster auf, dass abfragt welche SpielerInnen
# teilnehmen möchten.
def make_entry_player_window():
    rootwindow3 = tk.Toplevel()

    #rootwindow2.iconbitmap('./assets/Dice_Icon.ico')
    rootwindow3.title("Best Kniffel")
    rootwindow3.geometry("420x600")
    rootwindow3.resizable(False, False)

    top_frame = tk.Frame(
        rootwindow3,
        bg="orange",
        width=420,
        height=200
    )
    top_frame.place(x=0, y=0)

    middle_frame = tk.Frame(
        rootwindow3,
        bg="green",
        width=420,
        height=200,
    )
    middle_frame.place(x=0, y=200)

    bottom_frame = tk.Frame(
        rootwindow3,
        bg="red",
        width=420,
        height=200,
    )
    bottom_frame.place(x=0, y=400)

    label_player_entry = tk.Label(
        top_frame,
        bg="green",
        width=25,
        height=1,
        text="Tragen Sie eineN SpielerIn ein",
        font=("Arial", 15)
    )
    label_player_entry.place(x=80, y=140)

    text_player_entry = tk.Text(
        middle_frame,
        bg="black",
        fg="white",
        width=20,
        height=1,
        font=("Arial", 15)
    )
    text_player_entry.insert(
        index='1.0',
        chars='SpielerIn eintragen'
    )
    text_player_entry.place(x=100, y=40)
    text_player_entry.bind("<Button-1>", lambda event: text_player_entry.delete(0.0, tk.END))



    button_player_entry = tk.Button(
        bottom_frame,
        text="SpielerIn eintragen",
        bg="cyan",
        command = lambda: retrieve_player_name(text_player_entry)
    )
    button_player_entry.place(x=100, y=50)

    button_continue = tk.Button(
        bottom_frame,
        text="weiter",
        bg="cyan",
        command=lambda: (create_player_objects(), open_game(rootwindow3))
    )
    button_continue.place(x=230, y=50)

    rootwindow3.mainloop()