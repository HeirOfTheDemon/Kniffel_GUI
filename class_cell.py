import tkinter as tk
import class_dice_logic as dl


class Cell:

# Erstellt Constructor, der zwei Positionsargumente
# akzeptiert.
    def __init__(self, x, y):
        self.cell_button_object = None
        self.x = x
        self.y = y
        self.sum_tracked_dice = 0

# Erstellt Knopf um die Statistiken zu speichern
    def create_button_object(self, location):
        button_score = tk.Button(
            location,
            bg="orange",
            height=1,
            width=12,
        )
        button_score.bind("<Button-1>", self.left_click_action)
        self.cell_button_object = button_score

# Beim Linksklick wird die Anzahl der gewählten Würfel
# als Summe gespeichert
    def left_click_action(self,event):
        dl.get_result()
        self.cell_button_object.config(text=dl.result)