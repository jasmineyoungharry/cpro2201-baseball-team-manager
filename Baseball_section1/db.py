import csv

def read_players(filename="players.csv"):
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
                players.append([name, pos, ab, hits])
    except FileNotFoundError:
        return []
    return players

def write_players(players, filename="players.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for p in players:
            writer.writerow([p[0], p[1], p[2], p[3]])