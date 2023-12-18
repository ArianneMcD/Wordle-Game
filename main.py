import random
import sys

def main():
    answer = getRandomWord()
    attempts = 0

    while attempts < 6:
        random_word = input("Enter a 5 letter guess?\n")
        printGuessColors(random_word, answer)
        attempts += 1
        if random_word == answer:
            print(f"You Won! That took {attempts} guess(es).")
            break

    if random_word != answer and attempts >= 6:
        print(f"You lost. The answer was {answer}.")

     

# A helper method that prints the guess with the correct colors to the console.
def printGuessColors(guess, answer):
    for i in range(len(guess)):
        color = letterColor(i, guess, answer)
        print(guess[i] + " - " + color)


# A helper method that determines the color of the letter in the guess.
def letterColor(index, guess, answer):
    if guess[index] == answer[index]:
        return "Green"
    elif guess[index] in answer and guess[index] != answer[index]:
        return "Yellow"
    else:
        return "Red"


# A method that gets a random word from a file.
def getRandomWord():
    # Choose the word to be the answer for testing purposes.
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        file = open("words.txt", "r")
        # Strip removes the new line at the end of each word.
        words = [word.strip() for word in file.readlines()]
        file.close()
        return random.choice(words)


main()
