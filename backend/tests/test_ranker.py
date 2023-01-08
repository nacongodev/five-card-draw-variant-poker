from unittest import TestCase
from card import Card
from ranker import Ranker
from hand import Hand


class TestRanker(TestCase):
    def test_rank_hand(self):
        ranker = Ranker()

        hand = Hand()
        hand.add_card(Card('hearts', 1))
        hand.add_card(Card('hearts', 2))
        hand.add_card(Card('hearts', 3))
        hand.add_card(Card('hearts', 4))
        hand.add_card(Card('hearts', 5))
        self.assertEqual(ranker.rank_hand(hand), 'straight flush')

        hand = Hand()
        hand.add_card(Card('hearts', 1))
        hand.add_card(Card('hearts', 1))
        hand.add_card(Card('hearts', 1))
        hand.add_card(Card('hearts', 1))
        hand.add_card(Card('hearts', 5))
        self.assertEqual(ranker.rank_hand(hand), 'four of a kind')

        hand = Hand()
        hand.add_card(Card('hearts', 1))
        hand.add_card(Card('hearts', 1))
        hand.add_card(Card('hearts', 1))
        hand.add_card(Card('hearts', 5))
        hand.add_card(Card('hearts', 5))
        self.assertEqual(ranker.rank_hand(hand), 'full house')

        hand = Hand()
        hand.add_card(Card('hearts', 1))
        hand.add_card(Card('hearts', 2))
        hand.add_card(Card('hearts', 3))
        hand.add_card(Card('hearts', 4))
        hand.add_card(Card('hearts', 6))
        self.assertEqual(ranker.rank_hand(hand), 'flush')

        hand = Hand()
        hand.add_card(Card('hearts', 1))
        hand.add_card(Card('hearts', 2))
        hand.add_card(Card('hearts', 3))
        hand.add_card(Card('hearts', 4))
        hand.add_card(Card('spades', 5))
        self.assertEqual(ranker.rank_hand(hand), 'straight')

        hand = Hand()
        hand.add_card(Card('hearts', 1))
        hand.add_card(Card('hearts', 1))
        hand.add_card(Card('hearts', 1))
        hand.add_card(Card('spades', 5))
        hand.add_card(Card('spades', 5))
        self.assertEqual(ranker.rank_hand(hand), 'three of a kind')
