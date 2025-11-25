
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a classic Hangman word-guessing game in Python. Practice string manipulation, loops, conditionals, and random selection.

## 📝 Tasks

### 🛠️ Game Setup and Word Selection

#### Description
Set up the game and randomly select a word for the player to guess from a predefined list.

#### Requirements
Completed program should:

- Define a list of possible words
- Randomly select one word at the start of the game
- Display the word as blanks (e.g., _ _ _ _)

Example:
```python
import random
words = ['python', 'hangman', 'challenge']
word = random.choice(words)
```

### 🛠️ Gameplay Loop and User Interaction

#### Description
Implement the main game loop where the player guesses letters, and the game tracks progress and attempts.

#### Requirements
Completed program should:

- Accept letter guesses from the user
- Show current progress after each guess (e.g., p _ t _ o n)
- Track and display the number of incorrect guesses remaining
- End the game when the word is guessed or attempts are exhausted
- Display win or lose messages

Example:
```python
guesses = []
attempts = 6
while attempts > 0:
	# ... game logic ...
	pass
```
