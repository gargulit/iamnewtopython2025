print("STORY 1")
print("You wake up in a magical forest. There are two paths:")
print("1. Walk down the shady path")
print("2. Climb the sunny hill")

choice = input("What do you choose? (1 or 2): ")

if choice == "1":
    print("You walk along the shady path and find unicorns! 🦄")
elif choice == "2":
    print("You climb the sunny hill and see a sleeping dragon! 🐉")
else:
    print("I didn't understand your choice... try again.")
print("story 2.")
print("It's after school, and GUY hears a strange sound behind the library.")
print("She discovers a door she's never seen before.")

print("What should she do?")
print("1. Enter the secret room")
print("2. Call the principal")

choice1 = input("Your choice (1 or 2): ")

if choice1 == "1":
    print("\nGUY enters the room and finds... a time machine!")
    print("She can:")
    print("1. Travel to the past")
    print("2. Jump to the future")

    choice2 = input("What does she choose? (1 or 2): ")

    if choice2 == "1":
        print("\nShe travels to the past and meets the founder of the school!")
        print("He gives her a magical school notebook. 📘✨")
    elif choice2 == "2":
        print("\nShe jumps to the future and sees herself at age 25...")
        print("She’s a billionaire with her own tech company! 💼🚀")
    else:
        print("\nThat’s not a valid choice. The time machine shuts down. ❌")

elif choice1 == "2":
    print("\nThe principal arrives and looks around...")
    print("She whispers: 'You found it too? Now you're part of the Time Guard.' ⏳🕶️")
else:
    print("\nI didn't understand your choice. Try again next time.")
