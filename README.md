## Author Jasmine Youngharry
# CPRO 2201 Midterm Project  
## Baseball Team Manager

This project is a command-line Python application that manages a baseball team lineup.  
The program allows users to view, add, remove, and update players while storing player data in a CSV file.

---

## Features

- Display the team lineup
- Add a new player
- Remove a player
- Move a player in the lineup
- Edit a player's position
- Edit player statistics (at bats and hits)
- Calculate batting average
- Save and load player data using a CSV file

---

## Object-Oriented Design

The program uses object-oriented programming principles:

### Player Class
Represents a baseball player with the following attributes:

- First name
- Last name
- Position
- At bats
- Hits

The class also calculates the player's batting average.

### Lineup Class
Manages a collection of Player objects and provides methods to:

- Add players
- Remove players
- Move players in the lineup
- Access players by index

---

## File Handling

Player data is stored in a CSV file called:

```
players.csv
```

The `db.py` module handles:

- Reading player data from the CSV file
- Writing updated data back to the CSV file

---

## How to Run the Program

1. Open the project folder in VS Code.
2. Navigate to the desired project section (e.g., `project_section3`).
3. Run the program using Python:

```
python main.py
```

---

## Menu Options

The program provides the following options:

```
1 - Display lineup
2 - Add player
3 - Remove player
4 - Move player
5 - Edit player position
6 - Edit player stats
7 - Exit program
```

---

## Author

CPRO 2201 Midterm Project  
Baseball Team Manager