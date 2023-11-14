def calculate_score(rolls):
    score = 0
    go = 1
    roll_index = 0

    while go <= 10:
        if rolls[roll_index] == 10:  # Strike
            score += 10 + rolls[roll_index + 1] + rolls[roll_index + 2]
            roll_index += 1
        elif rolls[roll_index] + rolls[roll_index + 1] == 10:  # Spare
            score += 10 + rolls[roll_index + 2]
            roll_index += 2
        else:
            score += rolls[roll_index] + rolls[roll_index + 1]
            roll_index += 2
        go += 1
    return score

def play_bowling():
    rolls = []
    go = 1

    while go <= 10:
        print(f"Go {go}")
        roll1 = int(input("Enter the number of pins knocked down in the first go: "))

        if roll1 == 10:  # Strike
            rolls.append(roll1)
            go += 1
            continue

        roll2 = int(input("Enter the number of pins knocked down in the second go: "))

        if roll1 + roll2 > 10:
            print("Invalid input")
            continue

        rolls.append(roll1)
        rolls.append(roll2)
        go += 1

    score = calculate_score(rolls)
    print(f"\nYour final score is: {score}")


play_bowling()
