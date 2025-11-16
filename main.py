class Deck():
  def __init__(self):
    self.cards = [i for i in range(100)]

  def draw_card(self) -> int:
    if self.cards == []:
      return None
    
    return self.cards.pop()
  
  def reset(self) -> None:
    self.cards = [i for i in range(100)]

  def size(self) -> int:
    return len(self.cards)
  
  def is_empty(self) -> bool:
    return self.size() == 0
  
  def add_card(self, cards : list[int]) -> None:
    self.cards.extend(cards)
