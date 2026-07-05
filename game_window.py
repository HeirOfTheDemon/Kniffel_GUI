import tkinter as tk
from class_cell import Cell

def check_row_score_entry():
    pass

def make_game_window():
    rootwindow4 = tk.Toplevel()

    rootwindow4.iconbitmap('./assets/Dice_Icon.ico')
    rootwindow4.title("Best Kniffel")
    rootwindow4.geometry("420x600")
    rootwindow4.resizable(False, False)

    top_frame = tk.Frame(
        rootwindow4,
        bg="purple",
        width=420,
        height=30
    )
    top_frame.place(x=0, y=0)

    top_middle_frame = tk.Frame(
        rootwindow4,
        bg="orange",
        width=420,
        height=360
    )
    top_middle_frame.place(x=0, y=30)

    bottom_middle_frame = tk.Frame(
        rootwindow4,
        bg="green",
        width=420,
        height=180
    )
    bottom_middle_frame.place(x=0, y=390)

    bottom_frame = tk.Frame(
        rootwindow4,
        bg="red",
        width=420,
        height=30
    )
    bottom_frame.place(x=0, y=570)

    '''label_Kniffelblock = tk.Label(
        top_middle_frame,
        bg="green",
        text="Kniffelblock",
        font=("Arial", 15),
        width=10,
        height=1,
    )
    label_Kniffelblock.place(x=150, y=10)'''

    label_kniffelblock = tk.Label(
        top_middle_frame,
        bg="green",
        text="Kniffelblock",
        font=("Arial", 10),
    )
    label_kniffelblock.grid(row=0, column=0, columnspan=5)

    label_ones = tk.Label(
        top_middle_frame,
        bg="orange",
        text="Einser",
        font=("Arial", 7),
    )
    label_ones.grid(row=1, column=0, sticky="e")

    label_twos = tk.Label(
        top_middle_frame,
        bg="orange",
        text="Zweier",
        font=("Arial", 7),
    )
    label_twos.grid(row=2, column=0, sticky="e")

    label_threes = tk.Label(
        top_middle_frame,
        bg="orange",
        text="Dreier",
        font=("Arial", 7),
    )
    label_threes.grid(row=3, column=0, sticky="e")

    label_fours = tk.Label(
        top_middle_frame,
        bg="orange",
        text="Vierer",
        font=("Arial", 7),
    )
    label_fours.grid(row=4, column=0, sticky="e")

    label_fives = tk.Label(
        top_middle_frame,
        bg="orange",
        text="Fünfer",
        font=("Arial", 7),
    )
    label_fives.grid(row=5, column=0, sticky="e")

    label_sixes = tk.Label(
        top_middle_frame,
        bg="orange",
        text="Sechser",
        font=("Arial", 7),
    )
    label_sixes.grid(row=6, column=0, sticky="e")

    '''label_sum1 = tk.Label(
        top_middle_frame,
        bg="orange",
        text="Gesamt",
        font=("Arial", 7),
    )
    label_sum1.grid(row=7, column=0, sticky="e")'''

    '''label_bonus = tk.Label(
        top_middle_frame,
        bg="orange",
        text="Bonus >63",
        font=("Arial", 7),
    )
    label_bonus.grid(row=8, column=0, sticky="e")'''

    '''label_sum_upper = tk.Label(
        top_middle_frame,
        bg="orange",
        text="Gesamt oberer Teil",
        font=("Arial", 7),
    )
    label_sum_upper.grid(row=9, column=0, sticky="e")'''

    label_threes_double = tk.Label(
        top_middle_frame,
        bg="orange",
        text="Dreierpasch",
        font=("Arial", 7),
    )
    label_threes_double.grid(row=7, column=0, sticky="e")

    label_fours_double = tk.Label(
        top_middle_frame,
        bg="orange",
        text="Viererpasch",
        font=("Arial", 7),
    )
    label_fours_double.grid(row=8, column=0, sticky="e")

    label_full_house = tk.Label(
        top_middle_frame,
        bg="orange",
        text="Full House",
        font=("Arial", 7),
    )
    label_full_house.grid(row=9, column=0, sticky="e")

    label_small_street = tk.Label(
        top_middle_frame,
        bg="orange",
        text="Kleine Straße",
        font=("Arial", 7),
    )
    label_small_street.grid(row=10, column=0, sticky="e")

    label_big_street = tk.Label(
        top_middle_frame,
        bg="orange",
        text="Große Straße",
        font=("Arial", 7),
    )
    label_big_street.grid(row=11, column=0, sticky="e")

    label_kniffel = tk.Label(
        top_middle_frame,
        bg="orange",
        text="Kniffel",
        font=("Arial", 7),
    )
    label_kniffel.grid(row=12, column=0, sticky="e")

    label_chance = tk.Label(
        top_middle_frame,
        bg="orange",
        text="Chance",
        font=("Arial", 7),
    )
    label_chance.grid(row=13, column=0, sticky="e")

    '''label_sum_lower = tk.Label(
        top_middle_frame,
        bg="orange",
        text="Gesamt unterer Teil",
        font=("Arial", 7),
    )
    label_sum_lower.grid(row=17, column=0, sticky="e")'''

    '''label_sum_upper2 = tk.Label(
        top_middle_frame,
        bg="orange",
        text="Gesamt oberer Teil",
        font=("Arial", 7),
    )
    label_sum_upper2.grid(row=18, column=0, sticky="e")'''

    '''label_sum_game = tk.Label(
        top_middle_frame,
        bg = "orange",
        text="Endsumme",
        font=("Arial", 7),
    )
    label_sum_game.grid(row=14, column=0, sticky="e")'''

    for i in range (1, 14):
        for j in range (1, 5):
            button_cell = Cell(i, j)
            button_cell.create_button_object(top_middle_frame)
            button_cell.cell_button_object.grid(row=i, column=j)



    button_top_left_dice = tk.Button(
        bottom_middle_frame,
        text="1",
        bg="purple",
        width=5,
        height=2
    )
    button_top_left_dice.place(x=75, y=35)

    button_bottom_left_dice = tk.Button(
        bottom_middle_frame,
        text="2",
        bg="purple",
        width=5,
        height=2
    )
    button_bottom_left_dice.place(x=115, y=105)

    button_top_middle_dice = tk.Button(
        bottom_middle_frame,
        text="3",
        bg="purple",
        width=5,
        height=2
    )
    button_top_middle_dice.place(x=190, y=35)

    button_bottom_right_dice = tk.Button(
        bottom_middle_frame,
        text="4",
        bg="purple",
        width=5,
        height=2
    )
    button_bottom_right_dice.place(x=265, y=105)

    button_top_right_dice = tk.Button(
        bottom_middle_frame,
        text="5",
        bg="purple",
        width=5,
        height=2
    )
    button_top_right_dice.place(x=305, y=35)

    button_roll = tk.Button(
        bottom_frame,
        text="würfeln",
        bg="purple",
    )
    button_roll.place(x=180, y=2)

    rootwindow4.mainloop()
