score = 0
wickets = 0
ball = 0
overs = int(input("Enter number of overs: "))
total_balls = overs * 6
while ball < total_balls:
    overs_no = ball // 6 + 1
    ball_no = ball % 6 + 1
    print(f"over : {overs_no} - ball : {ball_no}")
    result = input("Enter the score : ")
    if result == "Wd":
        score += 1
        print("Wide! +1 run, Extra Ball")
    elif result == "Nb":
        score += 1
        print("No Ball! +1 run, Extra Ball")
    elif result == "W":
        wickets += 1
        ball += 1
        print("Wicket!")
        if wickets == 10:
            print("ALL OUT")
            break
    elif result in ["0", "1", "2", "3", "4", "6"]:
        score += int(result)
        ball += 1
    else:
        print("Invalid Input")
    if ball % 6 == 0 and ball != 0:
        print("\n--- End of Over", ball // 6, "---")
        print("Score:", score, "/", wickets)
print("\n------ SCORECARD ------")
print(f"Overs :{overs}")
print("Runs  :", score)
print("Wickets :", wickets)
