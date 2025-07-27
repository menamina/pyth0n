# wheel of fortune guessing game
import time
phrase = "As above so below".upper()
enteredPhrase = [ ]
phrase_letters = list(phrase)
trials = 0
total = trials =+ 1

print("\nLet's play .. Wheel of Fortune!")
time.sleep(2)
print("The phrase has 4 words and 14 letters: \n_ _  _ _ _ _ _  _ _  _ _ _ _ _")
time.sleep(3)
print("\nEnter the letters you think are in the phrase one at at a time. \nAt the end you will receieve your results")
time.sleep(2)


while True:
    guess = input("\nGuess one letter: ").upper()
    
    if guess in phrase_letters:
        print(f"\nThat is correct! {guess} is in our phrase!")

        # enter letters exactly where they are with _ _ _ _ _ ...

    if guess not in phrase_letters:
        print(f"\nThat is not correct. {guess} is NOT in our phrase!")

    elif guess == phrase:
        print("As above so below is our phrase! \n Thank you for playing.")
        print(f"And it only took you {total} number of guesses!")