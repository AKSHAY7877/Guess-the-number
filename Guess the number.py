#Guess the number by Akshay Sharma
n = 18
chances = 1
print("\t\t\tGuess the number \n")
while chances < 11:
    num = int(input("\nEnter number : "))
    if num > n:
        print("Greater value entered")
    elif num < n:
        print("Smaller value entered")
    else:
        print("Congratulation Player you win")
        exit(1)
    print("Chances left = ", (10-chances))
    chances += 1
print("\t\t\tYou Loose\n")
print("\t\t\tGame Over",  end="\n")
