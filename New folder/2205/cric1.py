# ==========================================
# CRICKET PLAYER STATISTICS MANAGEMENT
# ==========================================

# Player data
players = [
    {"id": 18, "name": "Virat Kohli", "matches": 254, "runs": 12000, "wickets": 41, "average": 58.67},
    {"id": 45, "name": "Rohit Sharma", "matches": 250, "runs": 10500, "wickets": 8, "average": 49.12},
    {"id": 7, "name": "M.S. Dhoni", "matches": 350, "runs": 10773, "wickets": 0, "average": 50.58},
    {"id": 10, "name": "Sachin Tendulkar", "matches": 463, "runs": 18426, "wickets": 11, "average": 44.83},
    {"id": 12, "name": "Yuvraj Singh", "matches": 304, "runs": 8701, "wickets": 24, "average": 36.55},
    {"id": 99, "name": "Jasprit Bumrah", "matches": 89, "runs": 320, "wickets": 149, "average": 8.89}
]


# ==========================================
# DISPLAY ALL PLAYERS
# ==========================================

def display_players(data):

    print("\nCRICKET PLAYER STATISTICS")
    print("-" * 70)

    for p in data:

        print("Player ID       :", p["id"])
        print("Player Name     :", p["name"])
        print("Matches         :", p["matches"])
        print("Runs            :", p["runs"])
        print("Wickets         :", p["wickets"])
        print("Batting Average :", p["average"])

        print("-" * 70)


# ==========================================
# QUICK SORT
# ==========================================

def quick_sort(data, key):

    # Base case
    if len(data) <= 1:
        return data

    # Select middle element as pivot
    pivot = data[len(data) // 2][key]

    # Elements smaller than pivot
    left = [p for p in data if p[key] < pivot]

    # Elements equal to pivot
    middle = [p for p in data if p[key] == pivot]

    # Elements greater than pivot
    right = [p for p in data if p[key] > pivot]

    # Recursively sort left and right
    return quick_sort(left, key) + middle + quick_sort(right, key)


# ==========================================
# SORT PLAYERS BY ID
# ==========================================

players = quick_sort(players, "id")


# ==========================================
# BINARY SEARCH BY PLAYER ID
# ==========================================

def binary_search_id(player_id):

    low = 0
    high = len(players) - 1

    while low <= high:

        mid = (low + high) // 2

        # Player found
        if players[mid]["id"] == player_id:
            return players[mid]

        # Search right half
        elif players[mid]["id"] < player_id:
            low = mid + 1

        # Search left half
        else:
            high = mid - 1

    return None


# ==========================================
# BINARY SEARCH BY PLAYER NAME
# ==========================================

def binary_search_name(name):

    # Create a copy sorted alphabetically
    data = quick_sort(players.copy(), "name")

    low = 0
    high = len(data) - 1

    name = name.lower()

    while low <= high:

        mid = (low + high) // 2

        middle_name = data[mid]["name"].lower()

        # Player found
        if middle_name == name:
            return data[mid]

        # Search right half
        elif middle_name < name:
            low = mid + 1

        # Search left half
        else:
            high = mid - 1

    return None


# ==========================================
# ADD NEW PLAYER
# ==========================================

def add_player():

    print("\nADD NEW PLAYER")
    print("-" * 30)

    player_id = int(input("Enter Player ID: "))

    # Check duplicate ID
    for p in players:

        if p["id"] == player_id:

            print("Player ID already exists!")
            return

    name = input("Enter Player Name: ")

    matches = int(input("Enter Matches: "))

    runs = int(input("Enter Runs: "))

    wickets = int(input("Enter Wickets: "))

    #average = float(input("Enter Batting Average: "))
    average=int((runs)/matches)

    # Create new player dictionary
    new_player = {

        "id": player_id,
        "name": name,
        "matches": matches,
        "runs": runs,
        "wickets": wickets,
        "average": average
    }


    # Add player to list
    players.append(new_player)


    # Sort again by ID
    # This is important for Binary Search
    players[:] = quick_sort(players, "id")


    print("\nPlayer added successfully!")


# ==========================================
# RANKING
# ==========================================

def ranking(key):

    # Create sorted copy
    data = quick_sort(players.copy(), key)

    # Reverse because ranking should be highest first
    data.reverse()

    print("\nRANKING BY", key.upper())
    print("-" * 50)

    for rank, p in enumerate(data, 1):

        print(rank, ".", p["name"], "->", p[key])


# ==========================================
# MAIN MENU
# ==========================================

while True:

    print("\n========== CRICKET STATISTICS ==========")

    print("1. Display All Players")
    print("2. Search by Player ID")
    print("3. Search by Player Name")
    print("4. Rank by Runs")
    print("5. Rank by Wickets")
    print("6. Rank by Batting Average")
    print("7. Add New Player")
    print("8. Exit")


    choice = int(input("Enter choice: "))


    # ======================================
    # DISPLAY PLAYERS
    # ======================================

    if choice == 1:

        display_players(players)


    # ======================================
    # SEARCH BY ID
    # ======================================

    elif choice == 2:

        player_id = int(input("Enter Player ID: "))

        result = binary_search_id(player_id)

        if result:

            display_players([result])

        else:

            print("Player not found.")


    # ======================================
    # SEARCH BY NAME
    # ======================================

    elif choice == 3:

        name = input("Enter Player Name: ")

        result = binary_search_name(name)

        if result:

            display_players([result])

        else:

            print("Player not found.")


    # ======================================
    # RANK BY RUNS
    # ======================================

    elif choice == 4:

        ranking("runs")


    # ======================================
    # RANK BY WICKETS
    # ======================================

    elif choice == 5:

        ranking("wickets")


    # ======================================
    # RANK BY BATTING AVERAGE
    # ======================================

    elif choice == 6:

        ranking("average")


    # ======================================
    # ADD NEW PLAYER
    # ======================================

    elif choice == 7:

        add_player()


    # ======================================
    # EXIT
    # ======================================

    elif choice == 8:

        print("Program ended.")

        break


    # ======================================
    # INVALID CHOICE
    # ======================================

    else:

        print("Invalid choice!")