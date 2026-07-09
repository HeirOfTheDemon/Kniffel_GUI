import tkinter as tk
import number_player_window
import interact_DB
from interact_DB import check_entry


# Öffnet ein Fenster, dass nach TeilnehmerInnen
# Anzahl fragt
def open_number_player(first_window, second_window, check):
    if check:
        first_window.withdraw()
        second_window = second_window.make_player_window()
    else:
        popup_denied = tk.Tk()
        popup_denied.title("ACCESS DENIED")
        popup_denied.geometry("300x50")

        label_denied = tk.Label(
            popup_denied,
            height=50,
            width=300,
            bg="black",
            fg="yellow",
            text="Wrong Login")
        label_denied.pack()
        popup_denied.mainloop()

# Erzeugt und populiert ein Fenster, in dem Benutzername
# und Passwort abgefragt werden und nur nach korrekter
# Eingabe weiterleitet
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

    text_username = tk.Text(
        middle_frame,
        bg="black",
        fg="white",
        width=20,
        height=1,
        font=("Arial", 15)
    )
    text_username.insert(
        index='1.0',
        chars='Username'
    )
    text_username.place(x=100, y=40)
    text_username.bind("<Button-1>", lambda event: text_username.delete(0.0, tk.END))

    entry_password = tk.Entry(
        middle_frame,
        bg="black",
        fg="white",
        width=20,
        font=("Arial", 15),
        show="*"
    )
    entry_password.place(x=100, y=80)

    '''text_password = tk.Text(
        middle_frame,
        bg="black",
        fg="white",
        width=20,
        height=1,
        font=("Arial", 15),
        show = "*"
    )
    text_password.insert(
        index='1.0',
        chars='Password'
    )
    text_password.place(x=100, y=80)
    text_password.bind("<Button-1>", lambda event: text_password.delete(0.0, tk.END))'''

    button_login = tk.Button(
        bottom_frame,
        text="Log In",
        bg="cyan",
    )
    button_login.place(x=180, y=50)
    #button_login.bind("<Button-1>", lambda x: number_player_window.make_player_window() )
    button_login.bind("<Button-1>", lambda x: open_number_player(
                        rootwindow,
                        number_player_window,
                        check_entry(text_username.get("1.0", "end-1c"), entry_password.get())
                        ))

    rootwindow.mainloop()

