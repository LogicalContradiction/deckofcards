from .deckofcardsenums import Suit, Value
from .const import DEFAULT_RANKS
import random

class Card():

	def __init__(self, value, suit):
		self.value = value
		self.suit = suit

	def eq(self, other, ranks=None):
		return self.__eq__(other, ranks)

	def __eq__(self, other, ranks=None):
		if not isinstance(other, Card):
			return NotImplemented
		self_rank = self.value.get_rank(ranks)
		other_rank = other.value.get_rank(ranks)
		if self_rank == other_rank and Suit.does_sort_by_suit(ranks):
			self_suit_rank = self.suit.get_rank(ranks)
			other_suit_rank = other.suit.get_rank(ranks)
			return self_rank == other_rank and self_suit_rank == other_suit_rank
		return self_rank == other_rank and self.suit == other.suit
	
	def lt(self, other, ranks=None):
		return self.__lt__(other, ranks)

	def __lt__(self, other, ranks=None):
		if not isinstance(other, Card):
			return NotImplemented
		self_rank = self.value.get_rank(ranks)
		other_rank = other.value.get_rank(ranks)
		if self_rank == other_rank and Suit.does_sort_by_suit(ranks):
			self_suit_rank = self.suit.get_rank(ranks)
			other_suit_rank = other.suit.get_rank(ranks)
			return self_suit_rank < other_suit_rank
		return self_rank < other_rank
	
	def le(self, other, ranks=None):
		return self.__le__(other, ranks)

	def __le__(self, other, ranks=None):
		if not isinstance(other, Card):
			return NotImplemented
		self_rank = self.value.get_rank(ranks)
		other_rank = other.value.get_rank(ranks)
		if self_rank == other_rank and Suit.does_sort_by_suit(ranks):
			self_suit_rank = self.suit.get_rank(ranks)
			other_suit_rank = other.suit.get_rank(ranks)
			return self_suit_rank <= other_suit_rank
		return self_rank <= other_rank
	
	def gt(self, other, ranks=None):
		return self.__gt__(other, ranks)

	def __gt__(self, other, ranks=None):
		if not isinstance(other, Card):
			return NotImplemented
		self_rank = self.value.get_rank(ranks)
		other_rank = other.value.get_rank(ranks)
		if self_rank == other_rank and Suit.does_sort_by_suit(ranks):
			self_suit_rank = self.suit.get_rank(ranks)
			other_suit_rank = other.suit.get_rank(ranks)
			return self_suit_rank > other_suit_rank
		return self_rank > other_rank
	
	def ge(self, other, ranks=None):
		return self.__ge__(other, ranks)

	def __ge__(self, other, ranks=None):
		if not isinstance(other, Card):
			return NotImplemented
		self_rank = self.value.get_rank(ranks)
		other_rank = other.value.get_rank(ranks)
		if self_rank == other_rank and Suit.does_sort_by_suit(ranks):
			self_suit_rank = self.suit.get_rank(ranks)
			other_suit_rank = other.suit.get_rank(ranks)
			return self_suit_rank >= other_suit_rank
		return self_rank >= other_rank

	def __repr__(self):
		return f"deckofcards.Card({repr(self.value)}, {repr(self.suit)})"

	def __str__(self):
		if self.value == Value.JOKER:
			return "joker"
		return f"{self.value} of {self.suit}"


class Deck():

	def __init__(self, num_jokers=0, shuffle=True, num_combine_decks=1):
		self.num_combine_decks = num_combine_decks
		self.num_jokers = num_jokers
		self.deck = self._create_deck(num_jokers, num_combine_decks)
		if shuffle:
			self.shuffle()

	def _create_deck(self, num_jokers=0, num_combine_decks=1):
		result = []
		for suit in list(Suit)[:-1]:
			for value in list(Value)[:-1]:
				for count in range(num_combine_decks):
					result.append(Card(value, suit))

		for count in range(num_jokers):
			result.append(Card(Value.JOKER, Suit.JOKER))
		return result

	def reset_deck(self, shuffle=True):
		result = self._create_deck(self.num_jokers, self.num_combine_decks)
		if shuffle:
			self.shuffle()
		self.deck = result

	def shuffle(self):
		random.shuffle(self.deck)

	def draw(self, num_cards=1):
		result = []
		for count in range(num_cards):
			result.append(self.deck.pop())
		return result

	def remove_one_card(self, value, suit):
		remove_card = Card(value, suit)
		self.deck.remove(remove_card)

	def add_one_card(self, card):
		self.deck.append(card)