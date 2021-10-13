# For the randomized questions

import random

# Just some reminders!

# Please change the file location on your computer. LINE 38

# Disclaimer: On questions worth more than 1000 points in Jeopardy and 2000 in Double Jeopardy, you will receive 
# or lose the point value the contestant won or lost in the actual game.

# Skips first line of Table

first_line = True

# Stores all game info

game = []

# Stores all regular Jeopardy! info

rd1 = [] 

# Stores score

score = 0

# Stores Double Jeopardy! info

rd2 = []

# Stores Final Jeopardy! info

fin = ""

# Combs database

hasbeenfound = False
file = open(r'C:\Users\garv.gaur\Desktop\Jeopardy Parser\Jeopardy.txt', "r", encoding = "utf-8")

# Game Number

game_num = str(input("Which game would you like?\n"))

# Skip first line:

for line in file:
    if first_line:
        first_line = False
        continue
    
    # Find all questions pertaining to the game
    
    if line[:line.find(",")] == game_num:
        game.append(line.strip("\n"))
        hasbeenfound = True
    elif hasbeenfound == False:
        continue
    else:
        file.close()
        break
    
# Separates game data into 3 rounds
    
for i in range(len(game)):
    if "Double Jeopardy!" in game[i]:
        rd2.append(game[i])
    elif "Final Jeopardy!" in game[i]:
        fin = game[i]
    elif "Jeopardy" in game[i]:
        rd1.append(game[i]) 
        
# Round 1 played

print("Jeopardy!")
for i in range(len(rd1)):
    rand = random.randint(0, len(rd1) - 1)
    q = rd1[rand]
    splitq = q.split(",")
    category = splitq[3]
    val = splitq[4:6]  
    
    # If comma in value

    if len(val[1]) > 5:
        val[1] = ""
    if len(val[0]) == 3:
        val[0] = val[0].replace("\"", "") + val[1].replace("\"", "")

    # Shows question, category, and dollar value of the question

    q_val = val[0]
    print(category + ", " + q_val)
    
    # This removes the question from the round bank
    
    rd1.pop(rand)
    question = []
    if len(q_val) > 5:
        question = splitq[6:len(splitq)-1]
    else:
        question = splitq[5:len(splitq)-1]
    for item in question:
        item = item.replace("\"", "")
    print(*question, sep = ",")
    
    # User based score add or subtract and answer show
    
    check = input("Press enter to show answer.")
    ans = splitq[len(splitq)-1:len(splitq)]
    print(*ans, sep = ",")
    cho = input("Would you like to add or subtract?(a or s)\n")
    
    # Score manipulation
    
    if "s" in cho:
        scoreadd = int(q_val.replace("$", ""))
        score = score - scoreadd
    else:
        scoreadd = int(q_val.replace("$", ""))
        score += scoreadd
    print("Your score is now", str(score) + ".")
    
# Round 2 Played: exact same process

print("Double Jeopardy!")
for i in range(len(rd2)):
    rand = random.randint(0, len(rd2) - 1)
    q = rd2[rand]
    splitq = q.split(",")
    category = splitq[3]
    val = splitq[4:6]
    if len(val[1]) > 5:
        val[1] = ""
    if len(val[0]) == 3:
        val[0] = val[0].replace("\"", "") + val[1].replace("\"", "")
    q_val = val[0]
    print(category + ", " + q_val)
    rd2.pop(rand)
    question = None
    if len(q_val) > 4:
        question = splitq[6:len(splitq)-1]
    else:
        question = splitq[5:len(splitq)-1]
    for item in question:
        item = item.replace("\"", "")
    print(*question, sep = ",")
    check = input("Press enter to show answer.")
    ans = splitq[len(splitq)-1:len(splitq)]
    print(*ans, sep = ",")
    cho = input("Would you like to add or subtract?(a or s)\n")
    if "s" in cho:
        scoreadd = int(q_val.replace("$", ""))
        score = score - scoreadd
    else:
        scoreadd = int(q_val.replace("$", ""))
        score += scoreadd
    print("Your score is now", str(score) + ".")
    
# Final wager

print("Final Jeopardy!")

# Print category and question

splitq = fin.split(",")
category = splitq[3]
print(category)

# Wager after category but before question

wager = int(input("What would you like to wager? (must be integer)\n"))
print(*splitq[5:len(splitq)-1], sep = ",")

# User based answer display and score manipulation based on final wager

check = input("Press enter to show answer.")
print(*splitq[len(splitq)-1:len(splitq)], sep = ",")
cho = input("Was the answer right or wrong? (r or w)")
if "w" in cho:
    score = score - wager
else:
    score += wager
    
# Final score!

print("Your final score is", str(score) + ".")