import tkinter as tk
from tkinter import *
import entry_player_window

def open_entry_player(firstwindow, secondwindow):
    firstwindow.withdraw()
    secondwindow.create()

number_players = 2

def button_arrow_up(text, number):
    number = number + 1
    text.delete("1.0", "end")
    text.insert(
        index='1.0',
        chars=f'{number}'
    )
    print(number)

def button_arrow_down(text, number):
    number = number - 1
    text.delete("1.0", "end")
    text.insert(
        index='1.0',
        chars=f'{number}'
    )
    print(number)

def make_player_window():

    rootwindow2 = tk.Toplevel()

    rootwindow2.iconbitmap('./assets/Dice_Icon.ico')
    rootwindow2.title("Best Kniffel")
    rootwindow2.geometry("420x600")
    rootwindow2.resizable(False, False)

    top_frame = tk.Frame(
        rootwindow2,
        bg="orange",
        width=420,
        height=200
    )
    top_frame.place(x=0, y=0)

    middle_frame = tk.Frame(
        rootwindow2,
        bg="green",
        width=420,
        height=200,
    )
    middle_frame.place(x=0, y=200)

    bottom_frame = tk.Frame(
        rootwindow2,
        bg="red",
        width=420,
        height=200,
    )
    bottom_frame.place(x=0, y=400)

    label_number_players = tk.Label(
        top_frame,
        bg="green",
        width=30,
        height=1,
        text="Wie viele Spieler wollen teilnehmen?",
        font=("Arial", 15)
    )
    label_number_players.place(x=40, y=140)

    text_number_player = tk.Text(
        middle_frame,
        bg="black",
        fg="white",
        width=2,
        height=2,
        font=("Arial", 15)
    )
    text_number_player.insert(
        index='1.0',
        chars=f'{number_players}'
    )
    text_number_player.place(x=185, y=28)
    text_number_player.bind("<Button-1>", lambda event: text_number_player.delete(0.0, tk.END))

    arrow_up_photo = PhotoImage(file='./assets/Arrow_Up.png')

    button_up = tk.Button(
        middle_frame,
        image=arrow_up_photo,
        height=20,
        width=40,
        command = lambda: button_arrow_up(text_number_player, number_players)
    )
    button_up.place(x=210, y=30)

    arrow_down_photo = PhotoImage(file='./assets/Arrow_Down.png')

    button_down = tk.Button(
        middle_frame,
        image=arrow_down_photo,
        height=20,
        width=40,
        command=lambda: button_arrow_down(text_number_player, number_players)
    )
    button_down.place(x=210, y=50)

    button_start = tk.Button(
        bottom_frame,
        text="Los geht's",
        bg="cyan",
    )
    button_start.place(x=190, y=50)
    button_start.bind("<Button-1>", lambda event: open_entry_player(rootwindow2, entry_player_window.make_entry_player_window()))

    rootwindow2.mainloop()