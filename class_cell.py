import tkinter as tk
import dice_logic as dl


class Cell:

# Erstellt Constructor, der zwei Positionsargumente
# akzeptiert.
    def __init__(self, row, column):
        self.cell_button_object = None
        self.row = row
        self.column = column
        self.sum_tracked_dice = 0

    def __repr__(self):
        self.stat

# Erstellt Knopf um die Statistiken zu speichern
    def create_button_object(self, location):
        button_score = tk.Button(
            location,
            bg="orange",
            height=1,
            width=5,
        )
        button_score.bind("<Button-1>", self.left_click_action)
        self.cell_button_object = button_score

# Beim Linksklick wird die Anzahl der gewählten Würfel
# als Summe gespeichert
    def left_click_action(self,event):
        event = int(f'{self.row}{self.column}')
        dl.get_result(event)
        self.cell_button_object.config(text=dl.result)