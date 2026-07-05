import tkinter as tk
import main
from class_player import Player

player_names = []

def create_player():
    pass

def retrieve_player_name(text):
    player_name = text.get("1.0", "end-1c")
    player_names.append(player_name)
    #object_create_player(player_names)
    print(player_names)

def make_entry_player_window():
    rootwindow3 = tk.Toplevel()
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



    button_continue = tk.Button(
        bottom_frame,
        text="Weiter",
        bg="cyan",
        command = lambda: retrieve_player_name(text_player_entry)
    )
    button_continue.place(x=190, y=50)

    rootwindow3.mainloop()