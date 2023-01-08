from unittest import TestCase
from card import Card


class TestCard(TestCase):
    def test_attributes(self):
        card = Card('hearts', 1)
        self.assertEqual(card.suit, 'hearts')
        self.assertEqual(card.rank, 1)
