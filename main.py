from cards import Deck

testDeck = Deck()

for card in testDeck.get_cards():
    print("name: ", card.get_card_name(), " value: ", card.get_value())
