Map = {
    "last_room": "0,0,0",
    "0,0,0":
        {
            "name": "starting room",
            "desc":
            """
            Du stehst in einer Sackgassen.
            Vor dir türmt sich eine hohe Mauer auf!
            """,
            "long_desc":
            """
            Eine gaaanz ganz lange Beschreibung!
            """,
            "exits": {"s": "0,0,-1"},
            # weight: float, r_min: int, r_max: int, l_min: int, l_max: int
            "item_gen": [90, 0, 1, 1, 1],
            "items": []
        },
    "0,0,-1":
        {
            "name": "ein neuer Raum",
            "desc":
            """
            Du hast dich aus der Sackgasse befreit!
            """,
            "long_desc":
            """
            Noch so ein ganz ganz ganz lange Beschreibung!
            """,
            "exits": {"n": "0,0,0", "o": "0,-1,-1", "w": "0,1,-1"},
            # weight: float, r_min: int, r_max: int, l_min: int, l_max: int
            "item_gen": [90, 0, 1, 1, 1],
            "items": []
        }
}
