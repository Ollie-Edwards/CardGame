import pytest
from shuffler import Shuffler
from cards import Card, Deck
from collections import Counter

# test on a list of 52 integers
deck = [i for i in range(52)]


def test_fisher_yates_shuffle():
    shuffled = Shuffler.fisher_yates_shuffle(deck.copy())
    # Check same numbers are present
    assert sorted(shuffled) == sorted(deck)

    # Check the order has changed
    assert shuffled != deck

    # Shuffling shouldn't produce the same output twice in a row (most of the time)
    shuffle1 = Shuffler.fisher_yates_shuffle(deck.copy())
    shuffle2 = Shuffler.fisher_yates_shuffle(deck.copy())
    assert shuffle1 != shuffle2


def test_riffle_shuffle():
    shuffled = Shuffler.riffle_shuffle(deck.copy())
    # Check same numbers are present
    assert sorted(shuffled) == sorted(deck)

    # Check the order has changed
    assert shuffled != deck

    # Shuffling shouldn't produce the same output twice in a row (most of the time)
    shuffle1 = Shuffler.riffle_shuffle(deck.copy())
    shuffle2 = Shuffler.riffle_shuffle(deck.copy())
    assert shuffle1 != shuffle2


def test_strip_shuffle():
    shuffled = Shuffler.strip_shuffle(deck.copy())
    # Check same numbers are present
    assert sorted(shuffled) == sorted(deck)

    # Check the order has changed
    assert shuffled != deck

    # Shuffling shouldn't produce the same output twice in a row (most of the time)
    shuffle1 = Shuffler.strip_shuffle(deck.copy())
    shuffle2 = Shuffler.strip_shuffle(deck.copy())
    assert shuffle1 != shuffle2


def test_casino_style_shuffle():
    shuffled = Shuffler.casino_style_shuffle(deck.copy())
    # Check same numbers are present
    assert sorted(shuffled) == sorted(deck)

    # Check the order has changed
    assert shuffled != deck

    # Shuffling shouldn't produce the same output twice in a row (most of the time)
    shuffle1 = Shuffler.casino_style_shuffle(deck.copy())
    shuffle2 = Shuffler.casino_style_shuffle(deck.copy())
    assert shuffle1 != shuffle2
