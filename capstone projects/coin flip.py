import random

outcome = ["HEADS", "TAILS"]
h = 0
t = 0

while 1:
    ip = input("\nFlip coin (Y / N): ")
    
    if ip == ("Y" or "y"):
        toss = random.choice(outcome)
        if toss == "HEADS":
            h += 1
            print("-> HEADS")
            print(f"Heads, Tails = ({h},{t})")

        else:
            t += 1
            print("-> TAILS")
            print(f"Heads, Tails = ({h},{t})")
    
    elif ip == ("N" or "n"):
        print("Thank You :)")
        break

    else:
        print("Invalid choice :/")

        


