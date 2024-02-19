print('Welcome to my first game!')
name = input("What is your name? ").lower()
age = int(input("What is your age? ")).lower()

print("Hello", name, "you are", age, "years old")

if age >= 18:
    print("You are old enough to play!")
    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("Let's play!")
elif age >= 14:
    print("You can play with supervision.")
    supervision = input("Are you playing under supervision? ").lower()
    if supervision == "yes":
        print("Let's play")
    elif supervision == "no":
        print("Come back with a supervision")
else:
    print("You are not old enough to play.....")
