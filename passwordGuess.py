import random

words = [
    "apple", "banana", "grape", "orange", "peach", "pear", "plum", "kiwi", "mango", "melon"
]

password = random.choice(words)
size = len(password)
print("Welcome to the Password guessing Game!")
print(f"Guess the {size}- letter word.")

attempts = 0
def hint(guess,password):
    correct = []
    for i in range(min(len(guess),size)):
        if guess[i] == password[i]:
            correct.append(i+1)
    if correct:
        print(f"Hint: The Letters at positions {correct} are correct.")
    else:
        print("Hint: Way off! No letters are correct.")
    print("Try Again!")

while True:
    guess = input("Enter your guess: ").strip().lower()
    attempts += 1
    if guess == password:
        print(f"Congratulations! You have cracked the Password in {attempts} attempts.")
        break
    else:
        hint(guess,password)


