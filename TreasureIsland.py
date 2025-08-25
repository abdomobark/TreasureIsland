print("""
    \t\t\tWelcome to Treasure Island.
    \t\tYour mission is to find the treasure.\n
    """)

direction = input("Where do you want to go? Left or Right: ").lower()

if direction == "left":
    action = input("Swim or Wait? ").lower()
    if action == "swim":
        print("Attacked by trout. Game Over.")
    elif action == "wait":
        door = input("Which door? Red, Blue, or Yellow: ").lower()
        if door == "red":
            print("Burned by fire. Game Over.")
        elif door == "blue":
            print("Eaten by beasts. Game Over.")
        elif door == "yellow":
            print("🎉 YOU WIN! 🎉")
        else:
            print("Game Over.")
    else:
        print("Invalid choice. Game Over.")
else:
    print("Fall into a hole. Game Over.")
