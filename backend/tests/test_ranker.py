from unittest import TestCase
from card import Card
from ranker import Ranker


class TestRanker(TestCase):

    def test_is_straight_flush(self):
        ranker = Ranker()
        # Test a straight flush hand
        hand1 = [Card(5, 'hearts'), Card(6, 'hearts'), Card(7, 'hearts'), Card(8, 'hearts'), Card(9, 'hearts')]
        self.assertTrue(ranker.is_straight_flush(hand1))

        # Test a non-straight flush hand
        hand2 = [Card(5, 'hearts'), Card(6, 'hearts'), Card(7, 'hearts'), Card(8, 'hearts'), Card(9, 'spades')]
        self.assertFalse(ranker.is_straight_flush(hand2))

    def test_is_two_pair(self):
        ranker = Ranker()
        # Test a two pair hand
        hand1 = [Card(7, 'hearts'), Card(7, 'diamonds'), Card(14, 'clubs'), Card(14, 'spades'), Card(5, 'spades')]
        self.assertTrue(ranker.is_two_pair(hand1))

        # Test a hand that is not a two pair hand
        hand2 = [Card(7, 'hearts'), Card(7, 'diamonds'), Card(14, 'clubs'), Card(2, 'spades'), Card(5, 'spades')]
        self.assertFalse(ranker.is_two_pair(hand2))

    def test_is_pair(self):
        ranker = Ranker()
        # Test a pair hand
        hand1 = [Card(7, 'hearts'), Card(7, 'diamonds'), Card(14, 'clubs'), Card(2, 'spades'), Card(5, 'spades')]
        self.assertTrue(ranker.is_pair(hand1))

        # Test a hand that is not a pair hand
        hand2 = [Card(7, 'hearts'), Card(8, 'diamonds'), Card(14, 'clubs'), Card(2, 'spades'), Card(5, 'spades')]
        self.assertFalse(ranker.is_pair(hand2))
