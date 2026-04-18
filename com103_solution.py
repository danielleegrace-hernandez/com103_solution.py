heroes = [
    ("Layla", "Marksman"),
    ("Tigreal", "Tank"),
    ("Gusion", "Assassin"),
    ("Kagura", "Mage"),
    ("Chou", "Fighter")
]

# --- FUNCTION: CHECK IF NUMBER ---
def is_number(text):
    if text == "":
        return False
    i = 0
    while i < len(text):
        if text[i] < '0' or text[i] > '9':
            return False
        i += 1
    return True

# --- USER INFO ---
valid = False
while not valid:
    ign = input("In-game name (IGN): ")
    if ign.strip() != "":
        valid = True
    else:
        print("Invalid input. Please try again.")

valid = False
while not valid:
    rank = input("Current rank: ")
    if rank.strip() != "":
        valid = True
    else:
        print("Invalid input. Please try again.")

print("\n==========================================")
print("   MOBILE LEGENDS -- HERO ROSTER")
print("==========================================")

i = 0
while i < len(heroes):
    print(str(i+1) + ". " + heroes[i][0] + " [" + heroes[i][1] + "]")
    i += 1

print("==========================================")

matches = []

# --- MATCH INPUT ---
match_count = 1
while match_count <= 4:
    print("\n--- MATCH " + str(match_count) + " ---")

    # HERO NUMBER
    valid = False
    while not valid:
        hero_input = input("Hero number (0 to skip): ")
        if is_number(hero_input):
            hero_num = int(hero_input)
            if 0 <= hero_num <= 5:
                valid = True
            else:
                print("Invalid input. Enter 0 to 5.")
        else:
            print("Invalid input. Enter numbers only.")

    if hero_num != 0:
        hero_name = heroes[hero_num - 1][0]

        # KILLS
        valid = False
        while not valid:
            kills_input = input("Kills: ")
            if is_number(kills_input):
                kills = int(kills_input)
                valid = True
            else:
                print("Invalid input. Enter a number.")

        # DEATHS
        valid = False
        while not valid:
            deaths_input = input("Deaths: ")
            if is_number(deaths_input):
                deaths = int(deaths_input)
                valid = True
            else:
                print("Invalid input. Enter a number.")

        # ASSISTS
        valid = False
        while not valid:
            assists_input = input("Assists: ")
            if is_number(assists_input):
                assists = int(assists_input)
                valid = True
            else:
                print("Invalid input. Enter a number.")

        # RESULT
        valid = False
        while not valid:
            result = input("Result (W/L): ")
            result = result.lower()

            if result == 'w' or result == 'l':
                result = result.upper()
                valid = True
            else:
                print("Invalid input. Enter W or L.")

        # COMPUTE KDA
        if deaths == 0:
            death = 1
        else:
            death = deaths

        KA = (kills + assists) / death

        # TAG
        if KA >= 5 and result == 'W':
            tag = "DOMINATION!"
        elif KA >= 5 and result == 'L':
            tag = "Carried Hard"
        elif KA < 5 and result == 'W':
            tag = "Team Effort"
        else:
            tag = "Better Luck Next Game"

        matches.append({
            "hero": hero_name,
            "kda": KA,
            "result": result,
            "tag": tag
        })

    match_count += 1

# --- SUMMARY ---
wins = 0
losses = 0

i = 0
while i < len(matches):
    if matches[i]["result"] == 'W':
        wins += 1
    else:
        losses += 1
    i += 1

total = len(matches)

if total > 0:
    win_rate = int((wins / total) * 100)
else:
    win_rate = 0

# BEST MATCH
best_index = -1
best_KA = -1

i = 0
while i < len(matches):
    if matches[i]["kda"] > best_KA:
        best_KA = matches[i]["kda"]
        best_index = i
    i += 1

# --- OUTPUT ---
print("\n=============================================")
print("     " + ign + " -- MATCH LOG (" + rank + ")")
print("=============================================")

i = 0
while i < len(matches):
    m = matches[i]

    if m["result"] == 'W':
        result_text = "WIN"
    else:
        result_text = "LOSS"

    print("[" + str(i+1) + "] " + m["hero"] +
          " | KDA: " + format(m["kda"], ".2f") +
          " | " + result_text +
          " | " + m["tag"])
    i += 1

print("---------------------------------------------")
print("Matches Played :", total)
print("Wins :", wins, "| Losses :", losses)
print("Win Rate :", str(win_rate) + "%")

if best_index != -1:
    best_match = matches[best_index]
    print("Best Match : [" + str(best_index+1) + "] " +
          best_match["hero"] +
          " (KDA: " + format(best_match["kda"], ".2f") + ")")

print("=============================================")