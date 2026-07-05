import tkinter as tk
import number_player_window

def open_number_player(first_window, second_window):
    first_window.withdraw()
    second_window.create()

def make_login_window():
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
        width=20,
        height=1,
        text="Loggen Sie sich ein",
        font=("Arial", 15)
    )
    log_in_label.place(x=100, y=140)

    username = tk.Text(
        middle_frame,
        bg="black",
        fg="white",
        width=20,
        height=1,
        font=("Arial", 15)
    )
    username.insert(
        index='1.0',
        chars='Username'
    )
    username.place(x=100, y=40)
    username.bind("<Button-1>", lambda event: username.delete(0.0, tk.END))

    password = tk.Text(
        middle_frame,
        bg="black",
        fg="white",
        width=20,
        height=1,
        font=("Arial", 15)
    )
    password.insert(
        index='1.0',
        chars='Password'
    )
    password.place(x=100, y=80)
    password.bind("<Button-1>", lambda event: password.delete(0.0, tk.END))

    button_login = tk.Button(
        bottom_frame,
        text="Log In",
        bg="cyan",
    )
    button_login.place(x=190, y=50)
    button_login.bind("<Button-1>", lambda x: open_number_player(rootwindow, number_player_window.make_player_window()))

    rootwindow.mainloop()

