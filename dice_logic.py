import game_window as gw

result = 0

def get_result(event):
    global result
    result = 0
    result_dices = gw.list_all_dice
    print(event)

    if 10 < event < 20:
        for j in range(len(result_dices)):
            if result_dices[j] == 1:
                result += 1
                print(f'1: {result}')
                return result
    if 20 < event < 30:
        for j in range(len(result_dices)):
            if result_dices[j] == 2:
                result += 2
                print(f'2: {result}')
                return result
    if 30 < event < 40:
        for j in range(len(result_dices)):
            if result_dices[j] == 3:
                result += 3
                print(f'3: {result}')
                return result
    if 40 < event < 50:
        for j in range(len(result_dices)):
            if result_dices[j] == 4:
                result += 4
                print(f'4: {result}')
                return result
    if 50 < event < 60:
        for j in range(len(result_dices)):
            if result_dices[j] == 5:
                result += 5
                print(f'5: {result}')
                return result
    if 60 < event < 70:
        for j in range(len(result_dices)):
            if result_dices[j] == 6:
                result += 6
                print(f'6: {result}')
                return result
    if 70 < event < 90:
        result = sum(result_dices)
        return result
    if 90 < event < 100:
        result = 25
        return result
    if 100 < event < 110:
        result = 30
        return result
    if 110 < event < 120:
        result = 40
        return result
    if 120 < event < 130:
        result = 50
        return result
    if 130 < event < 140:
        result = sum(result_dices)
        return result








