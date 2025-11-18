from cards import Card, Deck
import pytest


def test_number_card_value():
    card = Card("7", "H")
    assert card.value == 7

    card = Card("2", "S")
    assert card.value == 2


def test_ace_card_value():
    card = Card("A", "D")
    assert card.value == 1


def test_face_cards_value():
    for rank in ["J", "Q", "K"]:
        card = Card(rank, "D")
        assert card.value == 0


def test_unknown_cards_value():
    with pytest.raises(Exception):
        card = Card("X", "D")

    with pytest.raises(Exception):
        card = Card("Q", "Y")


def test_get_card_name():
    card = Card("3", "S")
    assert card.get_card_name() == "3 of S"

    card = Card("Q", "D")
    assert card.get_card_name() == "Q of D"


def test_deck_starts_with_52_cards():
    deck = Deck()
    assert deck.size() == 52


def test_draw_reduces_size_by_one():
    deck = Deck()
    card = deck.draw_card()
    assert card is not None
    assert isinstance(card, Card)
    assert deck.size() == 51


def test_draw_from_empty_deck():
    deck = Deck()

    for i in range(52):
        card = deck.draw_card()
        assert card is not None
        assert isinstance(card, Card)
        assert deck.size() == (52 - (i + 1))

    card = deck.draw_card()
    assert card == None
    assert deck.size() == 0


def test_deck_isempty():
    deck = Deck()
    assert deck.is_empty() == False

    for i in range(52):
        _ = deck.draw_card()

    assert deck.is_empty() == True


def test_add_single_card_to_top_of_deck():
    deck = Deck()

    card = Card("A", "S")

    deck.add_card(card)
    assert deck.size() == 53
    assert deck.draw_card() == card


def test_add_multiple_cards_to_top_of_deck():
    deck = Deck()

    cards = [Card("A", "S"), Card("4", "C"), Card("10", "D"), Card("6", "H")]

    deck.add_cards(cards)
    assert deck.size() == 56

    assert deck.draw_card() == cards[-1]
    assert deck.draw_card() == cards[-2]
    assert deck.draw_card() == cards[-3]
    assert deck.draw_card() == cards[-4]


def test_get__all__cards():
    deck = Deck()

    cards = deck.get_cards()

    assert len(cards) == 52
    assert isinstance(cards[0], Card)
