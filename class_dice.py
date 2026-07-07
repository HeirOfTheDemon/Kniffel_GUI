import tkinter as tk
import random

class Dice:

    list_dice=[]
    list_dice_tracked=[]

# Erzeugt Constructor, der zwei Attribute akzeptiert
    def __init__(self, id_dice, button):
        self.id_dice = id_dice
        self.button = button
        self.is_button_pressed = False
        self.roll = 0


# Auf Knopfdruck wird der Wüfel nicht mehr gewürfelt
    def keep_dice(self, button):
        if not self.is_button_pressed:
            button.config(bg="orange")
            self.is_button_pressed = True
            return self.is_button_pressed
        else:
            button.config(bg="purple")
            self.is_button_pressed = False

#  Wenn bestimmter Knopf nicht gedrückt, dann wird gewürfelt
    def roll_dice(self):
        if not self.is_button_pressed:
            image_roll = tk.PhotoImage(file="./assets/Dice_Six.png")
            self.roll = random.randint(1, 6)
            if self.roll == 1:
                image_roll = tk.PhotoImage(file="./assets/Dice_One.png")
            elif self.roll == 2:
                image_roll = tk.PhotoImage(file="./assets/Dice_Two.png")
            elif self.roll == 3:
                image_roll = tk.PhotoImage(file="./assets/Dice_Three.png")
            elif self.roll == 4:
                image_roll = tk.PhotoImage(file="./assets/Dice_Four.png")
            elif self.roll == 5:
                image_roll = tk.PhotoImage(file="./assets/Dice_Five.png")
            elif self.roll == 6:
                image_roll = tk.PhotoImage(file="./assets/Dice_Six.png")

            self.button.config(bg="purple")
            self.button.image = image_roll
            self.button.config(image=image_roll)
            #self.list_dice.append(roll)

    '''def tracked_dice(self):
        tracker = -1
        if self.is_button_pressed:
            tracker = self.list_dice[self.id_dice]
            self.list_dice_tracked.append(tracker)
        print(f'{self.list_dice_tracked} : {self.id_dice}')'''