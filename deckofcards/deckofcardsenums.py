from enum import Enum


class Suit(Enum):
	CLUB = 1
	DIAMOND = 2
	HEART = 3
	SPADE = 4

	def __repr__(self):
		return f"deckofcardsenums.Suit.{self.name}"

	def __str__(self):
		return f"{self.name.lower()}s"




class Value(Enum):
	TWO = 2
	THREE = 3
	FOUR = 4
	FIVE = 5
	SIX = 6
	SEVEN = 7
	EIGHT = 8
	NINE = 9
	TEN = 10
	JACK = 11
	QUEEN = 12
	KING = 13
	ACE = 14

	def __repr__(self):
		return f"deckofcardsenums.Value.{self.name}"

	def __str__(self):
		if self == Value.JACK \
		or self == Value.QUEEN \
		or self == Value.KING \
		or self == Value.ACE:
			return self.name.lower()
		return str(self.value)

	def __lt__(self, other):
		if not isinstance(other, Value):
			return NotImplemented
		return self.value < other.value

	def __le__(self, other):
		if not isinstance(other, Value):
			return NotImplemented
		return self.value <= other.value

	def __gt__(self, other):
		if not isinstance(other, Value):
			return NotImplemented
		return self.value > other.value

	def __ge__(self, other):
		if not isinstance(other, Value):
			return NotImplemented
		return self.value >= other.value

	