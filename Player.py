from dataclasses import dataclass
from Items import Item, Weapon, Armor
from typing import List
import random


@dataclass
class Race:
    strength_bonus: int = 0
    dexterity_bonus: int = 0
    constitution_bonus: int = 0
    intelligence_bonus: int = 0
    base_hitpoints: int = 0


@dataclass
class Dwarf(Race):  # Zwerg
    def __init__(self):
        self.strength_bonus = 6
        self.constitution_bonus = 8
        self.intelligence_bonus = -2
        self.base_hitpoints = 16

    def __repr__(self):
        return "Zwerg"


@dataclass
class Human(Race):  # Mensch
    def __init__(self):
        self.strength_bonus = 4
        self.dexterity_bonus = 2
        self.constitution_bonus = 4
        self.intelligence_bonus = 4
        self.base_hitpoints = 12

    def __repr__(self):
        return "Mensch"


@dataclass
class Elf(Race):  # Elf
    def __init__(self):
        self.strength_bonus = -2
        self.intelligence_bonus = 8
        self.constitution_bonus = 4
        self.dexterity_bonus = 4
        self.base_hitpoints = 12

    def __repr__(self):
        return "Elf"


@dataclass
class Gnome(Race):  # Gnom
    def __init__(self):
        self.strength_bonus = -2
        self.intelligence_bonus = 4
        self.dexterity_bonus = 8
        self.base_hitpoints = 10

    def __repr__(self):
        return "Gnom"


@dataclass
class Player:
    name: str
    race: Race
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int
    max_hitpoints: int
    current_hp: int
    max_weight: int
    ac: int
    atk: int
    inventory: List[Item]
    equipment: dict[str, Item]
    current_weight: int = 0

    def __init__(self, name: str, race: Race):
        self.name = name
        self.race = race
        # get random attributes
        self.strength = random.choice(range(6, 10)) + self.race.strength_bonus
        self.dexterity = random.choice(range(6, 10)) + self.race.dexterity_bonus
        self.constitution = random.choice(range(6, 10)) + self.race.constitution_bonus
        self.intelligence = random.choice(range(6, 10)) + self.race.intelligence_bonus
        # calculate other attributes
        self.max_hitpoints = self.race.base_hitpoints + self.constitution * 2
        self.current_hp = self.max_hitpoints
        self.max_weight = int(self.strength * 10 / 3)
        self.ac = 10 + self.dexterity
        self.atk = self.strength
        self.inventory = []
        self.equipment = {}

    def __repr__(self):
        return f"{self.name} ({self.race}) - str:{self.strength} dex:{self.dexterity} " \
               f"con:{self.constitution} int:{self.intelligence} hp:{self.current_hp} "

    def update_hp(self, hp_loss_gain: int):
        update = self.current_hp + hp_loss_gain
        if update > self.max_hitpoints:
            self.current_hp = self.max_hitpoints
        elif update <= 0:
            self.current_hp = 0
            print(f"{self.name} stirbt!")
        else:
            self.current_hp = update

    def regen(self):  # regenerate all hp!
        self.current_hp = self.max_hitpoints
        print("Maximale HP hergestellt!")

    def add_item(self, item: Item):
        check = self.current_weight + item.weight
        if check > self.max_weight:
            print(f"\nZu schwer!\nDu kannst leider nicht mehr als {self.max_weight} kg tragen!")
        else:
            self.inventory.append(item)
            self.current_weight += item.weight

    def show_inventory(self):
        print(f"\nGewicht: {self.current_weight} Max: {self.max_weight}")
        for item in self.inventory:
            if item in self.equipment.values():
                print(":: (->)", item)
            else:
                print("::", item)

    def equip(self, item: Item):
        if item.item_class == "armor":
            match item.item_subclass:
                case "head":
                    if "head" in self.equipment:
                        self.ac -= self.equipment["head"].ac_bonus
                    self.equipment["head"] = item
                case "body":
                    if "body" in self.equipment:
                        self.ac -= self.equipment["body"].ac_bonus
                    self.equipment["body"] = item
                case "feet":
                    if "feet" in self.equipment:
                        self.ac -= self.equipment["feet"].ac_bonus
                    self.equipment["feet"] = item

            self.ac += item.ac_bonus
            print(f"{item.name} ausgerüstet!")

        elif item.item_class == "weapon":
            if "weapon" in self.equipment:
                self.atk -= self.equipment["weapon"].atk_bonus
            self.equipment["weapon"] = item

            self.atk += item.atk_bonus

        else:
            print(f"{item.name} kann nicht ausgerüstet werden!")

