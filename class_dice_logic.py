import game_window as gw
import class_cell as cc

result = 0

def get_result():
    global result
    result = 0
    result_dices = gw.list_all_dice
    print(result_dices)

    for i in range(1, 5):
        if cc.Cell(1,i):
            result = 0
            for j in range(len(result_dices)):
                if result_dices[j] == 1:
                    result += 1








