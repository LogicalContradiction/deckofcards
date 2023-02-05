import unittest
import inspect

from deckofcards import deckofcards
from deckofcards.deckofcardsenums import Suit, Value

class AoC_2022_Puzzle_13_Tests(unittest.TestCase):

	def test_card_eq(self):
		card1 = deckofcards.Card(Value.TEN, Suit.CLUB)
		card2 = deckofcards.Card(Value.TEN, Suit.CLUB)
		card3 = deckofcards.Card(Value.TEN, Suit.DIAMOND)
		card4 = deckofcards.Card(Value.ACE, Suit.CLUB)
		card5 = deckofcards.Card(Value.KING, Suit.SPADE)

		self.assertTrue(card1 == card2)
		self.assertFalse(card1 == card3)
		self.assertFalse(card2 == card4)
		self.assertFalse(card2 == card5)
		self.assertTrue(card1 != card3)

	def test_suit_repr(self):
		self.assertEqual(repr(Suit.CLUB), "deckofcardsenums.Suit.CLUB")
		self.assertEqual(repr(Suit.DIAMOND), "deckofcardsenums.Suit.DIAMOND")
		self.assertEqual(repr(Suit.SPADE), "deckofcardsenums.Suit.SPADE")
		self.assertEqual(repr(Suit.HEART), "deckofcardsenums.Suit.HEART")

	def test_suit_str(self):
		self.assertEqual(str(Suit.CLUB), "clubs")
		self.assertEqual(str(Suit.DIAMOND), "diamonds")
		self.assertEqual(str(Suit.SPADE), "spades")
		self.assertEqual(str(Suit.HEART), "hearts")

	def test_value_repr(self):
		self.assertEqual(repr(Value.TWO), "deckofcardsenums.Value.TWO")
		self.assertEqual(repr(Value.THREE), "deckofcardsenums.Value.THREE")
		self.assertEqual(repr(Value.FOUR), "deckofcardsenums.Value.FOUR")
		self.assertEqual(repr(Value.FIVE), "deckofcardsenums.Value.FIVE")
		self.assertEqual(repr(Value.SIX), "deckofcardsenums.Value.SIX")
		self.assertEqual(repr(Value.SEVEN), "deckofcardsenums.Value.SEVEN")
		self.assertEqual(repr(Value.EIGHT), "deckofcardsenums.Value.EIGHT")
		self.assertEqual(repr(Value.NINE), "deckofcardsenums.Value.NINE")
		self.assertEqual(repr(Value.TEN), "deckofcardsenums.Value.TEN")
		self.assertEqual(repr(Value.JACK), "deckofcardsenums.Value.JACK")
		self.assertEqual(repr(Value.QUEEN), "deckofcardsenums.Value.QUEEN")
		self.assertEqual(repr(Value.KING), "deckofcardsenums.Value.KING")
		self.assertEqual(repr(Value.ACE), "deckofcardsenums.Value.ACE")

	def test_value_str(self):
		self.assertEqual(str(Value.TWO), "2")
		self.assertEqual(str(Value.THREE), "3")
		self.assertEqual(str(Value.FOUR), "4")
		self.assertEqual(str(Value.FIVE), "5")
		self.assertEqual(str(Value.SIX), "6")
		self.assertEqual(str(Value.SEVEN), "7")
		self.assertEqual(str(Value.EIGHT), "8")
		self.assertEqual(str(Value.NINE), "9")
		self.assertEqual(str(Value.TEN), "10")
		self.assertEqual(str(Value.JACK), "jack")
		self.assertEqual(str(Value.QUEEN), "queen")
		self.assertEqual(str(Value.KING), "king")
		self.assertEqual(str(Value.ACE), "ace")

	def test_value_comparison(self):
		#gt
		self.assertTrue(Value.KING > Value.SEVEN)
		self.assertFalse(Value.SEVEN > Value.KING)
		#ge
		self.assertTrue(Value.KING >= Value.SEVEN)
		self.assertFalse(Value.SEVEN >= Value.KING)
		#lt
		self.assertTrue(Value.SEVEN < Value.KING)
		self.assertFalse(Value.KING < Value.SEVEN)
		#le
		self.assertTrue(Value.SEVEN <= Value.KING)
		self.assertFalse(Value.KING <= Value.SEVEN)

	def test_card_repr(self):
		card = deckofcards.Card(Value.TEN, Suit.CLUB)
		self.assertEqual(repr(card), "deckofcards.Card(deckofcardsenums.Value.TEN, deckofcardsenums.Suit.CLUB)")

	def test_card_str(self):
		card = deckofcards.Card(Value.TEN, Suit.CLUB)
		self.assertEqual(str(card), "10 of clubs")

	def test_card_comparison(self):
		card1 = deckofcards.Card(Value.TEN, Suit.CLUB)
		card2 = deckofcards.Card(Value.ACE, Suit.SPADE)
		card3 = deckofcards.Card(Value.KING, Suit.HEART)

		#lt
		self.assertTrue(card1 < card2)
		self.assertFalse(card2 < card1)
		#le
		self.assertFalse(card2 <= card1)
		self.assertTrue(card1 <= card2)
		#gt
		self.assertTrue(card2 > card3)
		self.assertFalse(card3 > card2)
		#ge
		self.assertTrue(card2 >= card3)
		self.assertFalse(card3 >= card2)
