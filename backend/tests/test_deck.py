from unittest import TestCase
from deck import Deck


class TestDeck(TestCase):
    def test_init(self):
        deck = Deck()
        self.assertEqual(deck.size(), 52)

    def test_shuffle(self):
        deck = Deck()
        cards = deck.cards[:]  # make a copy of the cards
        deck.shuffle()
        self.assertNotEqual(cards, deck.cards)

    def test_size(self):
        deck = Deck()
        self.assertEqual(deck.size(), 52)
        deck.draw(1)
        self.assertEqual(deck.size(), 51)
