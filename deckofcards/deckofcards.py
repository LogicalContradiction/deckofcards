from .deckofcardsenums import Suit, Value
import random

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
		if self.value == Value.JOKER:
			return "joker"
		return f"{self.value} of {self.suit}"


class Deck():

	def __init__(self, num_jokers=0, shuffle=True, num_combine_decks=1):
		self.num_decks = num_combine_decks
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

	def reset_deck(self, num_jokers=0, shuffle=True):
		result = self._create_deck(num_jokers)
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