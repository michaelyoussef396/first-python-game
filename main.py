print('Welcome to my first game!')
name = input("What is your name? ").lower()
age = int(input("What is your age? ")) 

health = 10


if age >= 18:
    print("You are old enough to play!")
    wants_to_play = input("Do you want to play? ").lower()

    if wants_to_play == "yes":
        print("Your are starting with", health, "health")
        print("Let's play!")

        left_or_right = input("First choice.... left or right (left/right)? ")
        if left_or_right == "left":
            ans = input("Nice, you followed the path and reached a lake... Do you swim across or go around (across/around)? ")
            if ans == "around":
                print("You went around and reahced the other side of the lake.")
            elif ans == "across":
                print("You managed to get across but were bit by a fish and lost 5 health.")
                health = 5

            ans = input("You notice a house and a river. Which do you go to (river/house)? ")
            if ans == "house":
                print("You go to the house and are greeted by the owner.. He doesn't like you and you lose 5 health")
                health -= 5

                if health <= 0:
                    print("You noe have 0 health and you lose the game...")
                else:
                    print("You have survived... you win!")
            else:
                print("You fell in the river and lost...")

        else:
            print("You fell down and lost...")
    else:
        print("Cya...")

else:
    print("You are not old enough to play.....")
