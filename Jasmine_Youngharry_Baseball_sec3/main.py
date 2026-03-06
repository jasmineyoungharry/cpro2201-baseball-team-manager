import db
import ui
from datetime import date
from objects import Player, Lineup
from pathlib import Path

LINE_LEN = 64
DASH = "-" * LINE_LEN
CSV_PATH = Path(__file__).with_name("players.csv")

def display_lineup(lineup: Lineup):
    print()
    print(" Player                     POS     AB      H    AVG")
    print(DASH)
    for i, p in enumerate(lineup, start=1):
        print(f"{i:<2} {p.full_name:<25} {p.position:<5} "
              f"{p.at_bats:>6} {p.hits:>6} {p.batting_average:>7.3f}")
    print()


def add_player(lineup: Lineup):
    print()
    first = input("First name: ").strip()
    last = input("Last name: ").strip()
    pos = ui.get_position("Position: ")
    ab = ui.get_nonneg_int("At bats: ")
    hits = ui.get_nonneg_int("Hits: ")

    try:
        player = Player(first, last, pos, ab, hits)
    except ValueError as e:
        print(e)
        return

    lineup.add_player(player)
    print(f"{player.full_name} was added.")


def remove_player(lineup: Lineup):
    print()
    number = ui.get_int("Number: ")
    idx = number - 1
    if idx < 0 or idx >= len(lineup):
        print("Invalid integer. Please try again.")
        return
    removed = lineup.remove_player(idx)
    print(f"{removed.full_name} was deleted.")


def move_player(lineup: Lineup):
    print()
    current_num = ui.get_int("Current lineup number: ")
    current_idx = current_num - 1
    if current_idx < 0 or current_idx >= len(lineup):
        print("Invalid integer. Please try again.")
        return

    selected = lineup.get_player(current_idx)
    print(f"{selected.full_name} was selected.")

    new_num = ui.get_int("New lineup number: ")
    new_idx = new_num - 1
    if new_idx < 0 or new_idx >= len(lineup):
        print("Invalid integer. Please try again.")
        return

    lineup.move_player(current_idx, new_idx)
    print(f"{selected.full_name} was moved.")


def edit_position(lineup: Lineup):
    print()
    number = ui.get_int("Lineup number: ")
    idx = number - 1
    if idx < 0 or idx >= len(lineup):
        print("Invalid integer. Please try again.")
        return

    p = lineup.get_player(idx)
    print(f"You selected {p.full_name} POS={p.position}")

    try:
        p.position = ui.get_position("Position: ")
    except ValueError as e:
        print(e)
        return

    print(f"{p.full_name} was updated.")


def edit_stats(lineup: Lineup):
    print()
    number = ui.get_int("Lineup number: ")
    idx = number - 1
    if idx < 0 or idx >= len(lineup):
        print("Invalid integer. Please try again.")
        return

    p = lineup.get_player(idx)
    ab = ui.get_nonneg_int("At bats: ")
    hits = ui.get_nonneg_int("Hits: ")

    try:
        p.update_stats(ab, hits)
    except ValueError as e:
        print(e)
        return

    print(f"{p.full_name} was updated.")


def main():
    current_date_str = date.today().isoformat()
    game_date_str, game_dt = ui.get_game_date()
    days_until = ui.days_until_game(game_dt)

    lineup = db.read_lineup(CSV_PATH)

    while True:
        ui.display_menu(current_date_str, game_date_str, days_until)
        option = input("Menu option: ").strip()

        if option == "1":
            display_lineup(lineup)
        elif option == "2":
            add_player(lineup)
            db.write_lineup(lineup, CSV_PATH)
        elif option == "3":
            remove_player(lineup)
            db.write_lineup(lineup, CSV_PATH)
        elif option == "4":
            move_player(lineup)
            db.write_lineup(lineup, CSV_PATH)
        elif option == "5":
            edit_position(lineup)
            db.write_lineup(lineup, CSV_PATH)
        elif option == "6":
            edit_stats(lineup)
            db.write_lineup(lineup, CSV_PATH)
        elif option == "7":
            print("Bye!")
            break
        else:
            print("Invalid menu option. Please try again.")
        print()


if __name__ == "__main__":
    main()