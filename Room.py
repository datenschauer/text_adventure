from typing import List
from Items import create_item


class Room:

    def __init__(self, name: str, desc: str, long_desc: str, exits: dict, items: List):
        self.name = name
        self.desc = desc
        self.long_desc = long_desc
        self.exits = exits
        self.items = []
        if len(items) > 0:
            self.items = [create_item(item, int(item.split("-")[1])) for item in items]

        print(self.get_desc())
        print(self.__str__())

    def get_desc(self):
        return self.desc

    def get_long_desc(self):
        return self.long_desc

    def get_exits(self):
        return self.exits

    def get_items(self):
        return self.items

    def delete_item(self, item):
        self.items.remove(item)

    def eval_command(self, command: str):
        pass

    def __repr__(self):
        return self.name, self.exits

    def __str__(self):
        return self.name, self.exits
