# Elevens (A Solitaire-Style Card Game)

## Rules of Elevens (Slightly Adjusted)

- **Setup:**  
  9 cards are laid face up, and the remaining cards form the draw pile.

- **Removing Cards:**  
  - Cards (A–10) must be removed in pairs so that their values sum to 11.  
    (All number cards have their face value, and Aces have a value of 1.)  
  - Face cards (J, Q, K) must be removed in triplets, where any 3 face cards can be removed at once.

- **Replacing Cards:**  
  Whenever cards are removed, they are replaced from the draw pile until the pile is empty.

- **Winning and Losing:**  
  - You win by clearing all cards from the board.  
  - You lose if no valid moves remain and cards are still on the board.  
  - In my version, this is not possible since cards are added to the board until there is at least one valid move.

- **Timing:**  
  In my version, the time to complete the game is recorded, so try to complete the game as quickly as possible!

---

## Modeling the Deck of Cards

I implemented both a class and deck class to model the standard deck of playing cards. The deck stores a list of class objects, while also having built in methods to populate the deck with the standard 52 card deck, it also facilitates drawing cards from the top of the deck, adding cards onto the deck, and checking the size of the deck or if the deck is empty.

The card class represents a single card, it ensures every card has a valid rank and suit, the built in methods can be used to determine the value of the card according to the game rules, the name of the card, and also contains a function which gets the file path to where an image of the card can be located.

  The `Deck` stores a list of `Card` objects and provides methods to:
  - Populate the deck with the standard 52 cards.
  - Draw cards from the top of the deck.
  - Add cards to the deck.
  - Check the size of the deck or whether it is empty.

**Card Class:**  
  The `Card` class represents a single card and ensures that every card has a valid rank and suit.  
  It includes methods to:
  - Determine the value of the card according to the game rules.
  - Get the name of the card.
  - Get the file path to an image representing the card.

---

## Shuffling

Implemented both a `riffle shuffle` and `strip shuffle`, and combined this into a `casino style shuffle` by combining both of these shuffles multiple times, to create a simulation style and emulate how shuffling might take place in the real world. I also implemented a `fisher yates shuffle` which produces a pseudo random shuffle of the deck, this can produce a completely unbiased permeation of the deck, whereas the casino style shuffle may introduce certain patterns or bias into the deck. In my program the fisher yates shuffle is selected by default however this can easily be changed to the casino shuffle.

All shuffling algorithms were implemented as static methods in a `Shuffler` class, allowing them to be called easily without creating an instance, while keeping the class-based structure to logically group related functionality. Furthermore all methods in this class were tested using PyTest, the coverage report for these tests can be found in github actions testing artifacts.

---

## Unit Testing and Linting with PyTest and GitHub Actions

All core functionality including the Card and Deck classes are tested with `PyTest` to ensure they produce the expected output, the unit tests have 100% coverage of these 2 classes and test edge cases as well as valid inputs, the coverage reports can be found in the `GitHub Actions` workflow artifact. These unit tests are run on every push to the GitHub repo to ensure that all core functionality remains correct. Furthermore, on every push automatic linting is performed using `SuperLinter` and `GitHub actions`, this ensures that all code in the repository has a uniform and maintainable style.

---

## PyGame / CLI

- Having implemented my game in a **CLI**, I added an additional option to play the game with a **graphical user interface (GUI)** using **PyGame**, allowing players to interact with the cards visually rather than through text input.

---

## Installation Instructions

1. **Clone the repository:**  
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

2. **Install requirements using requirements.txt:**
```bash
pip install -r requirements.txt
```

3. **Run tests with PyTest:**
```bash
pytest --cov=cards --cov-report=term-missing --cov-report=html:htmlcov
pytest --cov=shuffler --cov-report=term-missing --cov-report=html:htmlcov
```

4. Run the game or run in IDE
```bash
python main.py
```
