import csv

def read_players(filename="players.csv"):
    """
    Returns list of dictionaries:
      {"name": str, "position": str, "at_bats": int, "hits": int}
    CSV columns:
      name, position, at_bats, hits
    """
    players = []
    try:
        with open(filename, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) < 4:
                    continue

                name = row[0].strip()
                pos = row[1].strip().upper()

                try:
                    ab = int(row[2])
                    hits = int(row[3])
                except ValueError:
                    continue

                players.append({
                    "name": name,
                    "position": pos,
                    "at_bats": ab,
                    "hits": hits
                })
    except FileNotFoundError:
        return []

    return players


def write_players(players, filename="players.csv"):
    """Write list of dicts back to CSV."""
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for p in players:
            writer.writerow([p["name"], p["position"], p["at_bats"], p["hits"]])