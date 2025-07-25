# tarot card generator
# 78 cards in a deck
# options: 1 card read, 3 card spread, 5 card spread, 7.
# choose a topic: General (genie picks!), love, career, finance, health.

import random
import time

options = "general", "love", "career", "finance", "health"

tarot_cards = ["The Fool", "The Magician", "The High Priestess", "The Empress",
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
    "Queen of Pentacles", "King of Pentacles"]

side = ("in reverse", "right side up")

num_of_cards = (1, 5, 7)

def wait():
    time.sleep(3)


# ----------------------------PROGRAM BELOW------------------------------------- #


print("I see you're looking to get your fortune read.")
name = input("My name is Genie, and you are?: ")
wait()
print(f"What kind of reading would you like today?")
wait()
print("I can do general readings, love, career, finance, or health.")
wait()

wanted = input("Which would you like? 😊: ")


