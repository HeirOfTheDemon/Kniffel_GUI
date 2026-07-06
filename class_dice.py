import tkinter as tk
import random

class Dice:

# Erzeugt Constructor, der ein Attribut akzeptiert
    def __init__(self, is_button_pressed = False):
        self._is_button_pressed = is_button_pressed

# Auf Knopfdruck wird der Wüfel nicht mehr gewürfelt
    def keep_dice(self, button):
        button.config(bg="orange")
        print(f"shouldn't change value: {self}")
        return True

#  Wenn bestimmter Knopf nicht gedrückt, dann wird gewürfelt
    def roll_dice(self, button, is_button_pressed = False):
        if not is_button_pressed:
            image_roll = tk.PhotoImage(file="./assets/Dice_Six.png")
            roll = random.randint(1, 6)
            if roll == 1:
                image_roll = tk.PhotoImage(file="./assets/Dice_One.png")
            elif roll == 2:
                image_roll = tk.PhotoImage(file="./assets/Dice_Two.png")
            elif roll == 3:
                image_roll = tk.PhotoImage(file="./assets/Dice_Three.png")
            elif roll == 4:
                image_roll = tk.PhotoImage(file="./assets/Dice_Four.png")
            elif roll == 5:
                image_roll = tk.PhotoImage(file="./assets/Dice_Five.png")
            elif roll == 6:
                image_roll = tk.PhotoImage(file="./assets/Dice_Six.png")
            button.config(bg="purple")
            button.image = image_roll
            button.config(image=image_roll)