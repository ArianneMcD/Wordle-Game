# Wordle-Game
In the game Wordle, the user is trying to guess a secret 5 letter word. The user will type in a 5 letter guess, and the computer will share information about how close the guess is to the actual answer. 

If a letter in the guess exactly matches a letter in the answer (same letter and correct position), the letter will be marked green.

If a letter in the guess almost matches a letter in the answer (same letter, but incorrect position), the letter will be marked yellow.

If a letter in the guess doesn’t match a letter in the answer (guessed letter doesn’t exist in answer), the letter will be marked red. The actual game marks the letter gray, but we will mark it red to be super clear.

The user will use this information to then make another guess, and will keep guessing until they guess the answer (they win), or they run out of their 6 guesses (they lose).

Differences from Real Game
In our project, we will be doing the user input and output in the console (as opposed to an online web browser like the real game).

We will also assume that no answer or guess has duplicate letters (i.e. a guess like TOTEM is not allowed because it has 2 Ts).
