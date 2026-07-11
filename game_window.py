import tkinter as tk
from class_dice import Dice
from class_cell import Cell


roll_counter = 0
dices = []
list_all_dice = []
button_cell = None
'''global tracked_dice
tracked_dice = []'''

# Diese Funktion bekommt das Würfe-Label als Parameter
# prüft ob drei Würfe gemacht wurden und führt dann
# den Würfelvorgang aus und füllt eine Liste mit den
# Ergebnissen. Sie verändert auch das Label
def on_roll(lab_roll):
    global roll_counter
    if roll_counter == 3:
        roll_counter = 0
    global list_all_dice
    list_all_dice = []
    for dice in dices:
        dice.roll_dice()
        list_all_dice.append(dice.roll)
    #print(list_all_dice)
    roll_counter += 1
    lab_roll.config(text=f'Wurf: {roll_counter}/3')
    return list_all_dice

#Erster Versuch die Würfel zu verfolgen, die gedrückt wurden
'''def get_tracked_dice():
    tracked_dice = []
    for dice in dices:
        if dice.is_button_pressed:
            tracked_dice.append(dice.roll)
    print(f'(tracked: {tracked_dice}')
    return tracked_dice'''


# Erstelle und populiere das Spielfenster. Es werden
# Würfel und Statistiken angezeigt
def make_game_window():
    rootwindow4 = tk.Toplevel()

    # Ersetzt die Standard Funktion des Schließen-Knopfes [X]
    # in ein popup, dass fragt ob wirklich geschlossen werden soll.
    def on_close():
        close_popup = tk.Toplevel()
        close_popup.title("SCHLIEßEN")
        close_popup.geometry("400x150")
        close_popup.resizable(False, False)
        close_popup.configure(bg="black")

        button_yes = tk.Button(
            close_popup,
            bg="red",
            text="Schließen",
            font=("Arial", 15)
        )
        button_yes.place(x=75, y=50)
        button_yes.bind("<Button-1>", lambda x: rootwindow4.destroy())

        button_no = tk.Button(
            close_popup,
            bg="green",
            text="Weiterspielen",
            font=("Arial", 15),
            command= lambda: close_popup.destroy()
        )
        button_no.place(x=200, y=50)

    #rootwindow4.iconbitmap('./assets/Dice_Icon.ico')
    rootwindow4.title("Best Kniffel")
    rootwindow4.geometry("420x600")
    rootwindow4.resizable(False, False)
    rootwindow4.protocol("WM_DELETE_WINDOW", lambda: on_close())

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


# Kein Platz für so viele Fenster auf der gewählten
# Größe des Spielfensters
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

# Erstelle ein Netz aus Knöpfen, die für die
# SpielerInnen-Statistiken verwendet werden
    for i in range (1, 14):
        for j in range (1, 9):
            global button_cell
            button_cell = Cell(i, j)
            button_cell.create_button_object(top_middle_frame)
            button_cell.cell_button_object.grid(row=i, column=j)

# Misslungener Versuch die Zellen des Kniffelblocks
# einzeln anzusprechen
    '''for i in range (1, 14):
        for j in range (1, 5):
            button_cell(i, j).config(
                command = get_tracked_dice()
            )'''


    image_dice_one = tk.PhotoImage(file="./assets/Dice_One.png")
    image_dice_two = tk.PhotoImage(file="./assets/Dice_Two.png")
    image_dice_three = tk.PhotoImage(file="./assets/Dice_Three.png")
    image_dice_four = tk.PhotoImage(file="./assets/Dice_Four.png")
    image_dice_five = tk.PhotoImage(file="./assets/Dice_Five.png")
    #image_dice_six = tk.PhotoImage(file="./assets/Dice_Six.png")

# Würfelknöpfe werden erzeugt und ihnen wird die 'behalten' Funktion übergeben
    button_top_left_dice = tk.Button(
        bottom_middle_frame,
        image=image_dice_one,
        bg="purple",
        width=40,
        height=40
    )
    button_top_left_dice.place(x=75, y=35)
    button_top_left_dice.bind("<Button-1>", lambda first_button_pressed: dices[0].keep_dice(button_top_left_dice))

    button_bottom_left_dice = tk.Button(
        bottom_middle_frame,
        image=image_dice_two,
        bg="purple",
        width=40,
        height=40
    )
    button_bottom_left_dice.place(x=115, y=105)
    button_bottom_left_dice.bind("<Button-1>", lambda second_button_pressed: dices[1].keep_dice(button_bottom_left_dice))


    button_top_middle_dice = tk.Button(
        bottom_middle_frame,
        image=image_dice_three,
        bg="purple",
        width=40,
        height=40
    )
    button_top_middle_dice.place(x=190, y=35)
    button_top_middle_dice.bind("<Button-1>", lambda third_button_pressed: dices[2].keep_dice(button_top_middle_dice))

    button_bottom_right_dice = tk.Button(
        bottom_middle_frame,
        image=image_dice_four,
        bg="purple",
        width=40,
        height=40
    )
    button_bottom_right_dice.place(x=265, y=105)
    button_bottom_right_dice.bind("<Button-1>", lambda fourth_button_pressed: dices[3].keep_dice(button_bottom_right_dice))

    button_top_right_dice = tk.Button(
        bottom_middle_frame,
        image=image_dice_five,
        bg="purple",
        width=40,
        height=40
    )
    button_top_right_dice.place(x=305, y=35)
    button_top_right_dice.bind("<Button-1>", lambda fifth_button_pressed: dices[4].keep_dice(button_top_right_dice))

    label_roll = tk.Label(
        bottom_middle_frame,
        bg="orange",
        text="Wurf: 0/3",
        font=("Arial", 10),
    )
    label_roll.place(x=358, y=155)




    # Instanziere fünf Würfel-Objekte,
    # die verwendet werden um Kniffel zu spielen
    global dices
    dices = [Dice(0, button_top_left_dice),
             Dice(1, button_bottom_left_dice),
             Dice(2, button_top_middle_dice),
             Dice(3, button_bottom_right_dice),
             Dice(4, button_top_right_dice)]

    button_roll = tk.Button(
        bottom_frame,
        text="würfeln",
        bg="purple",
        command=lambda: [on_roll(label_roll)]
    )
    button_roll.place(x=180, y=2)

    rootwindow4.mainloop()
