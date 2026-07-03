import tkinter as tk

def make_entry_player_window():
    rootwindow = tk.Tk()
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

    label_player_entry = tk.Label(
        top_frame,
        bg="green",
        width=25,
        height=1,
        text="Tragen Sie eineN SpielerIn ein",
        font=("Arial", 15)
    )
    label_player_entry.place(x=80, y=140)

    player_entry = tk.Text(
        middle_frame,
        bg="black",
        fg="white",
        width=20,
        height=1,
        font=("Arial", 15)
    )
    player_entry.insert(
        index='1.0',
        chars='SpielerIn eintragen'
    )
    player_entry.place(x=100, y=40)
    player_entry.bind("<Button-1>", lambda event: player_entry.delete(0.0, tk.END))

    button_continue = tk.Button(
        bottom_frame,
        text="Weiter",
        bg="cyan",
    )
    button_continue.place(x=190, y=50)

    rootwindow.mainloop()