import csv
from objects import Player


def _split_full_name(full_name: str) -> tuple[str, str]:
    parts = full_name.strip().split()
    if not parts:
        return "", ""
    if len(parts) == 1:
        return parts[0], ""
    return " ".join(parts[:-1]), parts[-1]


def read_lineup(filename="players.csv") -> list[Player]:
    players: list[Player] = []
    try:
        with open(filename, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) < 4:
                    continue
                full_name, pos, ab, hits = row[0], row[1], row[2], row[3]
                first, last = _split_full_name(full_name)
                try:
                    players.append(Player(first, last, pos, int(ab), int(hits)))
                except ValueError:
                    # skip bad rows safely
                    continue
    except FileNotFoundError:
        return []
    return players


def write_lineup(players: list[Player], filename="players.csv") -> None:
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for p in players:
            writer.writerow([p.full_name, p.position, p.at_bats, p.hits])