import tkinter as tk
from tkinter import PhotoImage


def make_player_window():
    rootwindow = tk.Tk()

    rootwindow.iconbitmap('./assets/Dice_Icon.ico')
    rootwindow.title("Best Kniffel")
    rootwindow.geometry("420x600")
    rootwindow.resizable(False, False)

    top_frame = tk.Frame(
        rootwindow,
        bg="orange",
        width=420,
        height=200
    )
    top_frame.place(x=0, y=0)

    middle_frame = tk.Frame(
        rootwindow,
        bg="green",
        width=420,
        height=200,
    )
    middle_frame.place(x=0, y=200)

    bottom_frame = tk.Frame(
        rootwindow,
        bg="red",
        width=420,
        height=200,
    )
    bottom_frame.place(x=0, y=400)

    log_in_label = tk.Label(
        top_frame,
        bg="green",
        width=30,
        height=1,
        text="Wie viele Spieler wollen teilnehmen?",
        font=("Arial", 15)
    )
    log_in_label.place(x=40, y=140)

    number_player = tk.Text(
        middle_frame,
        bg="black",
        fg="white",
        width=2,
        height=2,
        font=("Arial", 15)
    )
    number_player.insert(
        index='1.0',
        chars='2'
    )
    number_player.place(x=185, y=28)
    number_player.bind("<Button-1>", lambda event: number_player.delete(0.0, tk.END))

    arrow_up_photo = PhotoImage(file='./assets/Arrow_Up.png')

    button_up = tk.Button(
        middle_frame,
        image=arrow_up_photo,
        height=20,
        width=40
    )
    button_up.place(x=210, y=30)

    arrow_down_photo = PhotoImage(file='./assets/Arrow_Down.png')

    button_down = tk.Button(
        middle_frame,
        image=arrow_down_photo,
        height=20,
        width=40
    )
    button_down.place(x=210, y=50)

    button_start = tk.Button(
        bottom_frame,
        text="Los geht's",
        bg="cyan",
    )
    button_start.place(x=190, y=50)

    rootwindow.mainloop()