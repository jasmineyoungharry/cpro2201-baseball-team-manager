import db
from datetime import date, datetime

POSITIONS = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")

LINE_LEN = 64
LINE = "=" * LINE_LEN
DASH = "-" * LINE_LEN


def get_days_until(game_dt):
    """Return days until game if future, else None."""
    if game_dt is None:
        return None
    today = date.today()
    if game_dt > today:
        return (game_dt - today).days
    return None


def display_menu(current_date_str, game_date_str, days_until):
    print(LINE)
    print("Baseball Team Manager".center(LINE_LEN))
    print()
    print(f"CURRENT DATE:  {current_date_str}")
    print(f"GAME DATE:     {game_date_str}")
    if days_until is not None:
        print(f"DAYS UNTIL GAME: {days_until}")
    print()
    print("MENU OPTIONS")
    print("1 - Display lineup")
    print("2 - Add player")
    print("3 - Remove player")
    print("4 - Move player")
    print("5 - Edit player position")
    print("6 - Edit player stats")
    print("7 - Exit program")
    print()
    print("POSITIONS")
    print(", ".join(POSITIONS))
    print(LINE)


def prompt_menu_option():
    return input("Menu option: ").strip()


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid integer. Please try again.")


def get_nonneg_int(prompt):
    while True:
        value = get_int(prompt)
        if value < 0:
            print("Invalid integer. Please try again.")
        else:
            return value


def get_position(prompt="Position: "):
    while True:
        pos = input(prompt).strip().upper()
        if pos in POSITIONS:
            return pos
        print("Invalid position. Please try again.")


def batting_average(at_bats, hits):
    if at_bats == 0:
        return 0.0
    return hits / at_bats


def display_lineup(players):
    print()
    print(" Player                     POS     AB      H    AVG")
    print(DASH)
    for i, p in enumerate(players, start=1):
        name = p["name"]
        pos = p["position"]
        ab = p["at_bats"]
        hits = p["hits"]
        avg = batting_average(ab, hits)

        # spaces (no tabs) + 3 decimals
        print(f"{i:<2} {name:<25} {pos:<5} {ab:>6} {hits:>6} {avg:>7.3f}")
    print()


def add_player(players):
    print()
    name = input("Name: ").strip()
    pos = get_position("Position: ")
    ab = get_nonneg_int("At bats: ")
    hits = get_nonneg_int("Hits: ")

    if hits > ab:
        print("Hits can't be greater than at bats.")
        return

    players.append({"name": name, "position": pos, "at_bats": ab, "hits": hits})
    print(f"{name} was added.")


def remove_player(players):
    print()
    number = get_int("Number: ")
    idx = number - 1

    if idx < 0 or idx >= len(players):
        print("Invalid integer. Please try again.")
        return

    removed = players.pop(idx)
    print(f"{removed['name']} was deleted.")


def move_player(players):
    print()
    current_num = get_int("Current lineup number: ")
    current_idx = current_num - 1

    if current_idx < 0 or current_idx >= len(players):
        print("Invalid integer. Please try again.")
        return

    selected = players[current_idx]
    print(f"{selected['name']} was selected.")

    new_num = get_int("New lineup number: ")
    new_idx = new_num - 1

    if new_idx < 0 or new_idx >= len(players):
        print("Invalid integer. Please try again.")
        return

    player = players.pop(current_idx)
    players.insert(new_idx, player)
    print(f"{player['name']} was moved.")


def edit_position(players):
    print()
    number = get_int("Lineup number: ")
    idx = number - 1

    if idx < 0 or idx >= len(players):
        print("Invalid integer. Please try again.")
        return

    p = players[idx]
    print(f"You selected {p['name']} POS={p['position']}")

    p["position"] = get_position("Position: ")
    print(f"{p['name']} was updated.")


def edit_stats(players):
    print()
    number = get_int("Lineup number: ")
    idx = number - 1

    if idx < 0 or idx >= len(players):
        print("Invalid integer. Please try again.")
        return

    p = players[idx]

    ab = get_nonneg_int("At bats: ")
    hits = get_nonneg_int("Hits: ")

    if hits > ab:
        print("Hits can't be greater than at bats.")
        return

    p["at_bats"] = ab
    p["hits"] = hits
    print(f"{p['name']} was updated.")


def main():

    current_date_str = date.today().isoformat()
    print(LINE)
    print("Baseball Team Manager".center(LINE_LEN))
    print()
    print(f"CURRENT DATE:  {current_date_str}")


    while True:
        game_date_str = input("GAME DATE: ").strip()
        try:
            game_dt = datetime.strptime(game_date_str, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Invalid date format. Please try again.")

    days_until = get_days_until(game_dt)

    # read CSV as dicts
    players = db.read_players("players.csv")

    while True:
        display_menu(current_date_str, game_date_str, days_until)
        option = prompt_menu_option()

        if option == "1":
            display_lineup(players)
        elif option == "2":
            add_player(players)
            db.write_players(players, "players.csv")
        elif option == "3":
            remove_player(players)
            db.write_players(players, "players.csv")
        elif option == "4":
            move_player(players)
            db.write_players(players, "players.csv")
        elif option == "5":
            edit_position(players)
            db.write_players(players, "players.csv")
        elif option == "6":
            edit_stats(players)
            db.write_players(players, "players.csv")
        elif option == "7":
            print("Bye!")
            break
        else:
            print("Invalid menu option. Please try again.")

        print()


if __name__ == "__main__":
    main()