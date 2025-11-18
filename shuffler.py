import random
from itertools import zip_longest


class Shuffler:
    @staticmethod
    def fisher_yates_shuffle(deck):
        for i in range(len(deck) - 1, 0, -1):
            j = random.randint(0, i)
            deck[i], deck[j] = deck[j], deck[i]
        return deck

    @staticmethod
    def riffle_shuffle(deck):
        card_num = len(deck)
        midpoint = random.randint(card_num // 3, 2 * card_num // 3)

        l, r = deck[:midpoint], deck[midpoint:]

        return [x for pair in zip_longest(l, r) for x in pair if x is not None]

    @staticmethod
    def strip_shuffle(deck):
        shuffled = []

        while deck:
            chunk_size = random.randint(1, max(1, len(deck) // 5))
            index = len(deck) - chunk_size

            chunk = deck[index:]
            deck = deck[:index]

            shuffled.extend(chunk)

        return shuffled

    @staticmethod
    def casino_style_shuffle(deck, shuffle_repetitions=3):
        for _ in range(shuffle_repetitions):
            deck = Shuffler.strip_shuffle(deck)

            deck = Shuffler.riffle_shuffle(deck)

        return deck
