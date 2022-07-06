from Game import Game, load_game, roll_dice
from Player import Player, Dwarf, Human, Elf, Gnome
from pathlib import Path


def create_player() -> Player:
    races = ["Mensch", "Zwerg", "Elf", "Gnom"]
    print("Was für eine Rasse möchtest du spielen?")

    for i in range(len(races)):
        print(f"[{i}] :: {races[i]}")

    race = int(input("Gib die Nummer ein: >> "))
    print(f"Ok! Du bist ein {races[race]}!")
    name = input("Wie möchtest du heißen?\nGib deinen Namen ein: >> ")
    print(f"Gut {name} - los geht's!")

    match races[race]:
        case "Mensch":
            return Player(name, Human())
        case "Zwerg":
            return Player(name, Dwarf())
        case "Elf":
            return Player(name, Elf())
        case "Gnom":
            return Player(name, Gnome())


def init_save_game() -> Game:
    save_game_path = Path.cwd() / "save_games"

    if any(save_game_path.iterdir()):
        match input("Spielstand vorhanden! Möchtest du einen laden?\n>> ").lower():
            case "ja" | "j":
                savegames = [file for file in save_game_path.iterdir()]
                for i in range(len(savegames)):
                    print(f"[{i}] :: {savegames[i].stem}")  # without .json part
                choice: int = int(input("Welchen möchtest du laden?\nGib die Nummer ein. >> "))
                load_path = Path.cwd() / "save_games" / savegames[choice]
                return Game(load_game(load_path), savegames[choice].stem)
            case _:
                p = create_player()
                return Game(player=p)


# start the game
if __name__ == '__main__':
    g = init_save_game()

    g.play()
