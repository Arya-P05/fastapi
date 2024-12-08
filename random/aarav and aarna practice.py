from random import randint

num = randint(1, 20)

user_num = int(input("Guess a number between 0 and 20: "))

while (user_num != num):
    print("nope, guess again.")
    user_num = int(input("Guess a number between 0 and 20: "))
    if (user_num == num):
        print("Yes you got it!")
        break
    else:
        continue

