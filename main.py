import login_window
import number_player_window
import entry_player_window
import game_window
from class_player import Player


def object_create_player(list):
    for player in list:
        list[player] = Player()


login_window.make_login_window()
#number_player_window.make_player_window()
#entry_player_window.make_entry_player_window()
#game_window.make_game_window()
