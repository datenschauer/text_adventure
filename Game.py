from Room import Room
from Map import Map
from pathlib import Path
from Interactions import interaction
from Player import Player
from Items import get_rand_items
import json
import sys
import random


def roll_dice(*dices: int) -> int:
    return sum([random.choice(range(1, dice+1)) for dice in dices])


def save_game(filename: str, world=Map) -> None:
    path = Path.cwd() / "save_games" / (filename + ".json")
    print(path)
    with open(path, "w") as file:
        file.write(json.dumps(world))
        print("\n--- Spielstand gespeichert! ---")


def load_game(filepath: Path) -> dict:
    with open(filepath, "r") as file:
        print("\n--- Spielstand geladen! ---")
        return json.load(file)


def quit_game() -> None:
    print("Tschüss!")
    sys.exit(0)


class Game:

    def __init__(self, player: Player, world: dict = Map, save_game_name: str = "T3gYsqsWkL79PF"):
        self.world = world
        self.player = player
        new_room = self.world[self.world["last_room"]]
        items = new_room["items"]
        if (len(new_room["item_gen"]) > 0) and (len(new_room["items"]) == 0):
            items = get_rand_items(*new_room["item_gen"])
            new_room["items"] = items
        self.current_room = Room(
            name=new_room["name"],
            desc=new_room["desc"],
            long_desc=new_room["long_desc"],
            exits=new_room["exits"],
            items=items
        )
        self.coord = self.world["last_room"]
        self.save_game_name = save_game_name

        print("-" * len(player.__repr__()))
        print(player)
        print("-" * len(player.__repr__()))

    def get_command(self, command: str) -> None:

        match command.lower().split():

            case ["schau", "herum"] | ["schaue", "dich", "um"] | ["schau", "dich", "um"]:
                print(self.current_room.get_long_desc())

            case ["durchsuche", "Raum"] | ["durchsuchen"]:

                if len(self.current_room.get_items()) >= 1:
                    print("Nach längerem Suchen findest du folgende Sachen:")

                    for i in range(len(self.current_room.get_items())):
                        print(f"[{i}] :: {self.current_room.get_items()[i]}")

                    try:
                        choice = int(input("\nMöchtest du eines davon nehmen? Gib die Nummer ein:\n>> "))
                        self.player.add_item(self.current_room.get_items()[choice])
                        print(f"Du hast {self.current_room.get_items()[choice]} genommen.")
                        self.current_room.delete_item(self.current_room.get_items()[choice])

                    except ValueError:
                        pass

                else:
                    print("Nichts wertvolles gefunden!")

            case ["gehe", "nach", direction] | ["gehe", "zu", direction]:

                if direction[0] in self.current_room.get_exits().keys():
                    self.coord = self.current_room.get_exits()[direction[0]]
                    self.world["last_room"] = self.coord
                    new_room = self.world[self.coord]
                    items = new_room["items"]

                    if (len(new_room["item_gen"]) > 0) and (len(new_room["items"]) == 0):
                        items = get_rand_items(*new_room["item_gen"])
                        new_room["items"] = items

                    self.current_room = Room(
                        name=new_room["name"],
                        desc=new_room["desc"],
                        long_desc=new_room["long_desc"],
                        exits=new_room["exits"],
                        items=items
                    )
                else:
                    print("Da geht es nicht lang!")

            case ["nimm", item]:
                self.player.add_item(item)
                self.world[self.coord][2] -= 1  # reduce max quantity of items in current room
                self.current_room.delete_item(item)

            case ["rüste", item, "aus"]:
                self.player.equip(item)

            case ["zeige", "inventar"] | ["inventar"]:
                self.player.show_inventory()

            case ["speicher"] | ["speichern"]:
                if self.save_game_name == "T3gYsqsWkL79PF":
                    save_game(input(">> Gib einen Namen für den Spielstand ein: "))
                else:
                    save_game(self.save_game_name, self.world)
                    print(f"In {self.save_game_name} gespeichert!")

            case ["spiel", "beenden"] | ["beenden"] | ["ende"]:
                quit_game()

            case _:
                interaction(command, self.coord)

    def play(self):

        while True:

            self.get_command(input("\n>> "))
