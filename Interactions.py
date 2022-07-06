def interaction(command: str, room: str) -> None:

    match room:

        case "0,0,0":
            match command.lower().split():
                case ["kletter", "auf", "die", "mauer"] | ["klettere", "auf", "mauer"]:
                    print("Die Mauer ist viel zu rutschig!\n"
                          "Schon nach wenigen Zentimetern rutschst du ab.")

        case _:
            print("Das verstehe ich leider nicht.")
