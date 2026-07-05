import tkinter as tk

class Cell:
    def __init__(self, x, y):
        self.cell_button_object = None
        self.x = x
        self.y = y

    def create_button_object(self, location):
        button_score = tk.Button(
            location,
            text=f"{self.x} : {self.y}",
            bg="orange",
            height=1,
            width=12,
        )
        button_score.bind("<Button-1>", self.left_click_action)
        self.cell_button_object = button_score

    def left_click_action(self, event):
        print(event)
        print(f"left click action")