import unittest
import inspect

from deckofcards import deckofcards
from deckofcards.deckofcardsenums import Suit, Value

class AoC_2022_Puzzle_13_Tests(unittest.TestCase):

	def test_card_eq(self):
		card1 = deckofcards.Card(Suit.CLUB, Value.TEN)
		card2 = deckofcards.Card(Suit.CLUB, Value.TEN)
		card3 = deckofcards.Card(Suit.DIAMOND, Value.TEN)
		card4 = deckofcards.Card(Suit.CLUB, Value.ACE)
		card5 = deckofcards.Card(Suit.SPADE, Value.KING)

		self.assertEqual(card1, card2)
		self.assertNotEqual(card1, card3)
		self.assertNotEqual(card2, card4)
		self.assertNotEqual(card2, card5)
