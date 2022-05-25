import random

MAX = 50
MIN = 1
total_guess = 0
number = random.randrange(MIN, MAX)
player = input("Hello, what's your name ?: ")
print(f"okay! {player} What number am I guessing between {MIN} and {MAX}")

while total_guess < 5:
    guess = int(input())
    total_guess += 1
    if guess < number:
        print("Your guess is too low")
        print("Try again:")
    if guess > number:
        print("Your guess is too high")
        print("Try again:")
    if guess == number:
        break

if guess == number:
    print(f"Yah! solved in { total_guess } attempts")
else:
    print(f"Sorry you failed, correct guess is: { number }")
