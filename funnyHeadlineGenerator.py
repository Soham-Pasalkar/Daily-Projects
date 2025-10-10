import random

subject = [
    "Virat Kohli",
    "Cristiano Ronaldo",
    "President Donald Trump",
    "PM Narendra Modi",
    "Shahrukh Khan",
    "Ed Sheeran",
    "Elon Musk",
    "Physics Wallah"
]

verb = [
    "buys",
    "sells",
    "hates",
    "loves",
    "plays",
    "creates",
    "destroys",
    "eats",
    "launches",
    "declares war on"
]

object = [
    "a Pani Puri",
    "a Bitcoin",
    "a new startup",
    "a new car",
    "a new girlfriend",
    "a new game",
    "a Pizza",
    "a Space Craft",
    "a bomb"
]

place = [
    "at Home",
    "at Red Fort",
    "at UN Meeting",
    "on Mars",
    "on Street",
    "in his Dreams"
]

while True:
    person = random.choice(subject)
    action = random.choice(verb)
    thing = random.choice(object)
    location = random.choice(place)
    print(f"{person} {action} {thing} {location}\n")
    again = input("Do you want to generate another headline? (yes/no)").strip().lower()
    if again != 'yes':
        break

print("Thank you for using the Funny Headline Generator!")
