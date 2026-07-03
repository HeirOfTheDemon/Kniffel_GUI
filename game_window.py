import tkinter as tk

def make_game_window():
    rootwindow = tk.Tk()

    rootwindow.iconbitmap('./assets/Dice_Icon.ico')
    rootwindow.title("Best Kniffel")
    rootwindow.geometry("420x600")
    rootwindow.resizable(False, False)

    top_frame = tk.Frame(
        rootwindow,
        bg="cyan",
        width=420,
        height=30
    )
    top_frame.place(x=0, y=0)

    top_middle_frame = tk.Frame(
        rootwindow,
        bg="orange",
        width=420,
        height=360
    )
    top_middle_frame.place(x=0, y=30)

    bottom_middle_frame = tk.Frame(
        rootwindow,
        bg="green",
        width=420,
        height=180
    )
    bottom_middle_frame.place(x=0, y=390)

    bottom_frame = tk.Frame(
        rootwindow,
        bg="red",
        width=420,
        height=30
    )
    bottom_frame.place(x=0, y=570)

    label_Kniffelblock = tk.Label(
        top_middle_frame,
        bg="green",
        text="Kniffelblock",
        font=("Arial", 15),
        width=10,
        height=1,
    )
    label_Kniffelblock.place(x=150, y=10)

    '''top_middle_frame.rowconfigure(0, weight=1)
    top_middle_frame.rowconfigure(1, weight=1)
    top_middle_frame.rowconfigure(2, weight=1)
    top_middle_frame.rowconfigure(3, weight=1)
    top_middle_frame.rowconfigure(4, weight=1)
    top_middle_frame.rowconfigure(5, weight=1)
    top_middle_frame.rowconfigure(6, weight=1)
    top_middle_frame.rowconfigure(7, weight=1)
    top_middle_frame.rowconfigure(8, weight=1)
    top_middle_frame.rowconfigure(9, weight=1)
    top_middle_frame.rowconfigure(10, weight=1)
    top_middle_frame.rowconfigure(11, weight=1)
    top_middle_frame.rowconfigure(12, weight=1)
    top_middle_frame.rowconfigure(13, weight=1)
    top_middle_frame.rowconfigure(14, weight=1)
    top_middle_frame.rowconfigure(15, weight=1)
    top_middle_frame.rowconfigure(16, weight=1)
    top_middle_frame.rowconfigure(17, weight=1)
    top_middle_frame.rowconfigure(18, weight=1)
    top_middle_frame.rowconfigure(19, weight=1)
    top_middle_frame.columnconfigure(0, weight=4)
    top_middle_frame.columnconfigure(1, weight=2)
    top_middle_frame.columnconfigure(2, weight=1)
    top_middle_frame.columnconfigure(3, weight=1)
    top_middle_frame.columnconfigure(4, weight=1)
    top_middle_frame.columnconfigure(5, weight=1)'''

    top_middle_frame.columnconfigure((0,1,2,4,5,6,7,8,9,10),weight = 1, uniform = "a")
    top_middle_frame.columnconfigure(3,weight = 10, uniform = "a")
    top_middle_frame.rowconfigure((0,1,2,3,4,5,6,7,8,9,10),weight = 1, uniform = "a")

    for x in range(10):
        for y in range(10):
            frame = tk.Frame(
                master=top_middle_frame,
                relief=tk.RAISED,
                borderwidth=1
            )
            frame.grid(row=x, column=y, sticky="nesw")  # line 13
            label = tk.Label(master=frame, text=f"\n\nrow {x}\t\t column {y}\n\n")
            label.pack()


    button_top_left_dice = tk.Button(
        bottom_middle_frame,
        text="1",
        bg="cyan",
        width=5,
        height=2
    )
    button_top_left_dice.place(x=75, y=35)

    button_bottom_left_dice = tk.Button(
        bottom_middle_frame,
        text="2",
        bg="cyan",
        width=5,
        height=2
    )
    button_bottom_left_dice.place(x=115, y=105)

    button_top_middle_dice = tk.Button(
        bottom_middle_frame,
        text="3",
        bg="cyan",
        width=5,
        height=2
    )
    button_top_middle_dice.place(x=190, y=35)

    button_bottom_right_dice = tk.Button(
        bottom_middle_frame,
        text="4",
        bg="cyan",
        width=5,
        height=2
    )
    button_bottom_right_dice.place(x=265, y=105)

    button_top_right_dice = tk.Button(
        bottom_middle_frame,
        text="5",
        bg="cyan",
        width=5,
        height=2
    )
    button_top_right_dice.place(x=305, y=35)

    button_roll = tk.Button(
        bottom_frame,
        text="würfeln",
        bg="cyan",
    )
    button_roll.place(x=180, y=2)

    rootwindow.mainloop()
