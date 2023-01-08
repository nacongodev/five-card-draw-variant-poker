from unittest import TestCase
from hand import Hand
from card import Card


class TestHand(TestCase):
    def test_add_card(self):
        hand = Hand()
        card = Card('hearts', 1)
        hand.add_card(card)
        self.assertIn(card, hand.cards)

