# tarot card generator
# 78 cards in a deck
# options: 1 card read, 3 card spread, 5 card spread, 7.
# choose a topic: General (genie picks!), love, career, finance, health.

import random
import time

options = ("general", "love", "career", "finance", "health")

tarot_cards = ("The Fool", "The Magician", "The High Priestess", "The Empress",
    "The Emperor", "The Hierophant", "The Lovers", "The Chariot",
    "Strength", "The Hermit", "Wheel of Fortune", "Justice",
    "The Hanged Man", "Death", "Temperance", "The Devil",
    "The Tower", "The Star", "The Moon", "The Sun",
    "Judgement", "The World", "Ace of Wands", "2 of Wands", "3 of Wands", "4 of Wands",
    "5 of Wands", "6 of Wands", "7 of Wands", "8 of Wands",
    "9 of Wands", "10 of Wands", "Page of Wands", "Knight of Wands",
    "Queen of Wands", "King of Wands",
    "Ace of Cups", "2 of Cups", "3 of Cups", "4 of Cups",
    "5 of Cups", "6 of Cups", "7 of Cups", "8 of Cups",
    "9 of Cups", "10 of Cups", "Page of Cups", "Knight of Cups",
    "Queen of Cups", "King of Cups",
    "Ace of Swords", "2 of Swords", "3 of Swords", "4 of Swords",
    "5 of Swords", "6 of Swords", "7 of Swords", "8 of Swords",
    "9 of Swords", "10 of Swords", "Page of Swords", "Knight of Swords",
    "Queen of Swords", "King of Swords",
    "Ace of Pentacles", "2 of Pentacles", "3 of Pentacles", "4 of Pentacles",
    "5 of Pentacles", "6 of Pentacles", "7 of Pentacles", "8 of Pentacles",
    "9 of Pentacles", "10 of Pentacles", "Page of Pentacles", "Knight of Pentacles",
    "Queen of Pentacles", "King of Pentacles")

side = ("in reverse", "upright")

num_of_cards = ("3", "5", "7")

random_side = random.choice(side)

random_3 = random.sample(tarot_cards, (3))
random_5 = random.sample(tarot_cards, (5))
random_7 = random.sample(tarot_cards, (7))


def wait():
    time.sleep(3)


# ----------------------------PROGRAM BELOW------------------------------------- #


print("I see you're looking to get your fortune read.")
name = input("My name is Genie, and you are?: ").capitalize()
wait()
print(f"Nice to meet you! What kind of reading would you like today?")
wait()
print("I can do 'general', 'love', 'career', 'finance', or 'health' readings.")
wait()

while True:
    wanted = input("\nWhich would you like? 😊: ").lower()

    while wanted not in options:
        print("\nThe options are: general, love, career, finance, and health.")
        wanted = input("Please choose from the options above 😊: ").lower()

    if wanted in options:
        spread = input("\nAnd would you like a 3, 5, or 7 card spread?: ")

        while spread not in num_of_cards:
            spread = input("\nPlease choose a 3, 5, 7 card spread: ")

        if spread in num_of_cards:
            print(f"A {spread} card {wanted} reading today? Okay! Hang tight while I shuffle the deck.")
            wait()

            if spread == "3":
                print("\nYour cards in the order they fell:")
                wait()
                for cardPulled in random_3:
                    print(f"{cardPulled} {random_side}")

            if spread == "5":
                print("\nYour cards in the order they fell:")
                wait()
                for cardPulled in random_5:
                    print(f"{cardPulled} {random_side}")

            if spread == "7":
                print("\nYour cards in the order they fell:")
                wait()
                for cardPulled in random_7:
                    print(f"{cardPulled} {random_side}")
        
            print(f"\nWell {name}, it was a pleasure to read your cards today. Would you like another one?")

            word = input("If so, just say the magic word 'magic' otherwise say the not magic word 'no': ").lower()

            if word == "no":
                print("\nThanks for stopping by, take care!")
                break

            if word == "magic":
                continue

