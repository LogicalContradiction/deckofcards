from enum import Enum
from .const import DEFAULT_RANKS


class Suit(Enum):
	CLUB = 1
	DIAMOND = 2
	HEART = 3
	SPADE = 4
	JOKER = 5

	def __repr__(self):
		return f"deckofcardsenums.Suit.{self.name}"

	def __str__(self):
		if self == Suit.JOKER:
			return f"{self.name.lower()}"
		return f"{self.name.lower()}s"
	
	def get_rank(self, ranks=None):
		key = self.name
		if ranks == None:
			return DEFAULT_RANKS["suits"][key]
		return ranks["suits"][key]
	
	@classmethod
	def does_sort_by_suit(self, ranks=None):
		if ranks == None:
			return bool(DEFAULT_RANKS["values"])
		return bool(ranks["values"])




class Value(Enum):
	ACE = 1
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
	JOKER = 14

	def __repr__(self):
		return f"deckofcardsenums.Value.{self.name}"

	def __str__(self):
		if self == Value.JACK \
		or self == Value.QUEEN \
		or self == Value.KING \
		or self == Value.ACE \
		or self == Value.JOKER:
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
	
	def get_rank(self, ranks=None):
		key = self.name
		if ranks==None:
			return DEFAULT_RANKS["values"][key]
		return ranks.values[key]

	