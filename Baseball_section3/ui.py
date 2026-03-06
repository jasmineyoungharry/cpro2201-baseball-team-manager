from datetime import date, datetime
from objects import POSITIONS

LINE_LEN = 64
LINE = "=" * LINE_LEN
DASH = "-" * LINE_LEN


def get_game_date():
    while True:
        raw = input("GAME DATE: ").strip()
        try:
            game_dt = datetime.strptime(raw, "%Y-%m-%d").date()
            return raw, game_dt
        except ValueError:
            print("Invalid date format. Please try again.")


def days_until_game(game_dt):
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