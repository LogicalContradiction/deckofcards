from .deckofcardsenums import Suit, Value

class Card():

	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

	def __eq__(self, other):
		if not isinstance(other, Card):
			return NotImplemented
		return self.value == other.value and self.suit == other.suit

	def __lt__(self, other):
		if not isinstance(other, Card):
			return NotImplemented
		return self.value < other.value

	def __le__(self, other):
		if not isinstance(other, Card):
			return NotImplemented
		return self.value <= other.value

	def __gt__(self, other):
		if not isinstance(other, Card):
			return NotImplemented
		return self.value > other.value

	def __ge__(self, other):
		if not isinstance(other, Card):
			return NotImplemented
		return self.value >= other.value

	def __repr__(self):
		return f"deckofcards.Card({repr(self.value)}, {repr(self.suit)})"

	def __str__(self):
		return f"{self.value} of {self.suit}"