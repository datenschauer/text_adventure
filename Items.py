from dataclasses import dataclass
from typing import List
from itemlist import itemlist
import random


class Item:
    name: str
    item_class: str
    weight: float
    level: int
    gold: float

    def __init__(self, name, weight, level, item_class, gold):
        self.name = name
        self.weight = weight
        self.level = level
        self.gold = gold
        self.item_class = item_class

    def __repr__(self):
        return f"{self.name} [{self.weight} kg]"


class Weapon(Item):
    atk_bonus: int

    def __init__(self, name, weight, level, gold, atk_bonus, item_class="weapon"):
        super().__init__(name, weight, level, item_class, gold)
        self.atk_bonus = atk_bonus
        self.name = name
        self.weight = weight
        self.level = level
        self.gold = gold

    def __repr__(self):
        return f"+{self.atk_bonus} {self.name} [{self.weight} kg]"


class Armor(Item):
    ac_bonus: int
    item_subclass: str

    def __init__(self, name, weight, level, gold, ac_bonus, item_subclass, item_class="armor"):
        super().__init__(name, weight, level, item_class, gold)
        self.ac_bonus = ac_bonus
        self.name = name
        self.weight = weight
        self.gold = gold
        self.level = level
        self.item_subclass = item_subclass

    def __repr__(self):
        return f"+{self.ac_bonus} {self.name} [{self.weight} kg]"


def create_item(item: str, level: int) -> Item:
    match item[0]:
        case "w":
            return Weapon(
                name=itemlist[level][item]["name"].split()[0],
                weight=itemlist[level][item]["weight"],
                level=itemlist[level][item]["level"],
                gold=itemlist[level][item]["gold"],
                atk_bonus=itemlist[level][item]["atk_bonus"]
            )
        case "a":
            return Armor(
                name=itemlist[level][item]["name"].split()[0],
                weight=itemlist[level][item]["weight"],
                level=itemlist[level][item]["level"],
                gold=itemlist[level][item]["gold"],
                ac_bonus=itemlist[level][item]["ac_bonus"],
                item_subclass=itemlist[level][item]["item_subclass"]
            )
        case _:
            return Item(
                name=itemlist[level][item]["name"].split()[0],
                item_class=itemlist[level][item]["item_class"],
                weight=itemlist[level][item]["weight"],
                level=itemlist[level][item]["level"],
                gold=itemlist[level][item]["gold"]
            )


def get_rand_items(probability: float, r_min: int, r_max: int, l_min: int, l_max: int) -> List[Item]:
    if random.choices([True, False], weights=[probability, 100 - probability], k=1):
        quantity = random.choice(range(r_min, r_max+1))
        items = []
        for i in range(quantity + 1):
            level = random.choice(range(l_min, l_max+1))
            items.append(random.choice(list(itemlist[level].keys())))
        return [item for item in items]
    return []
