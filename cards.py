class Card:
  def __init__(self, rank, suit):
    self.rank = rank
    self.suit = suit
    self.value = self.get_value()

  def get_card_name(self):
    return self.rank + " of " + self.suit

  def get_value(self):
    ''' 
      Face cards must be removed in triplets only
      Ace has a value of 1
      Number cards are worth their face value
    '''
    if self.rank in ["J", "Q", "K"]:
      return 0
    
    elif self.rank == "A":
      return 1
    
    elif self.rank.isdigit():
      return int(self.rank)
    
    else:
      print(self.rank)
      raise Exception("Tried to find value of an unknown card")


class Deck:
  def __init__(self):
    self.cards = []
    self.reset()

  def draw_card(self) -> int:
    if self.cards == []:
      return None
    
    return self.cards.pop()
  
  def reset(self) -> None:
    self.cards = []

    suits = ["H", "D", "C", "S"]
    ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    for rank in ranks:
      for suit in suits:
        self.cards.append(Card(rank, suit))

  def size(self) -> int:
    return len(self.cards)
  
  def is_empty(self) -> bool:
    return self.size() == 0
  
  def add_card(self, cards : list[Card]) -> None:
    self.cards.extend(cards)

  def get_cards(self):
    return self.cards