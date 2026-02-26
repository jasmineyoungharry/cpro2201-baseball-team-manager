import db
from pathlib import Path

POSITIONS = ("C", "1B", "2B", "3B", "SS", "LF", "CF", "RF", "P")

LINE_LEN = 64
LINE = "=" * LINE_LEN
DASH = "-" * LINE_LEN
CSV_PATH = Path(__file__).with_name("players.csv")

def display_menu():
    print(LINE)
    print("Baseball Team Manager")
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


def avg(ab, hits):
    if ab == 0:
        return 0.0
    return hits / ab


def first_name_only(full_name):
    parts = full_name.strip().split()
    return parts[0] if parts else ""


def display_lineup(players):
    print()
    print("  Player                 POS     AB      H    AVG")
    print(DASH)
    for i, p in enumerate(players, start=1):
        name, pos, ab, hits = p
        shown = first_name_only(name)  
        print(f"{i:<2} {shown:<20} {pos:<5} {ab:>6} {hits:>6} {avg(ab, hits):>7.3f}")
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

    players.append([name, pos, ab, hits])
    print(f"{name} was added.")


def remove_player(players):
    print()
    number = get_int("Number: ")
    idx = number - 1
    if idx < 0 or idx >= len(players):
        print("Invalid integer. Please try again.")
        return
    removed = players.pop(idx)
    print(f"{removed[0]} was deleted.")


def move_player(players):
    print()
    current_num = get_int("Current lineup number: ")
    current_idx = current_num - 1
    if current_idx < 0 or current_idx >= len(players):
        print("Invalid integer. Please try again.")
        return

    selected = players[current_idx]
    print(f"{selected[0]} was selected.")

    new_num = get_int("New lineup number: ")
    new_idx = new_num - 1
    if new_idx < 0 or new_idx >= len(players):
        print("Invalid integer. Please try again.")
        return

    player = players.pop(current_idx)
    players.insert(new_idx, player)
    print(f"{player[0]} was moved.")


def edit_position(players):
    print()
    number = get_int("Lineup number: ")
    idx = number - 1
    if idx < 0 or idx >= len(players):
        print("Invalid integer. Please try again.")
        return

    p = players[idx]
    print(f"You selected {p[0]} POS={p[1]}")
    p[1] = get_position("Position: ")
    print(f"{p[0]} was updated.")


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

    p[2] = ab
    p[3] = hits
    print(f"{p[0]} was updated.")


def main():
    players = db.read_players(CSV_PATH)

    while True:
        display_menu()
        option = input("Menu option: ").strip()

        if option == "1":
            display_lineup(players)
        elif option == "2":
            add_player(players)
            db.write_players(players, CSV_PATH)
        elif option == "3":
            remove_player(players)
            db.write_players(players, CSV_PATH)
        elif option == "4":
            move_player(players)
            db.write_players(players, CSV_PATH)
        elif option == "5":
            edit_position(players)
            db.write_players(players, CSV_PATH)
        elif option == "6":
            edit_stats(players)
            db.write_players(players, CSV_PATH)
        elif option == "7":
            print("Bye!")
            break
        else:
            print("Invalid menu option. Please try again.")
        print()


if __name__ == "__main__":
    main()