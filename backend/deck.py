import random
from card import Card
from ranker import Ranker
from hand import Hand


class Deck:
    def __init__(self):
        self.cards = []
        self.ranker = Ranker()
        for suit in ['♥', '♠', '♦', '♣']:
            for rank in range(1, 14):
                self.cards.append(Card(suit=suit, rank=rank))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self, n):
        if self.size() < n:
            raise ValueError('Not enough cards in deck')
        hand = Hand()
        for i in range(n):
            hand.add_card(self.cards.pop())
        hand.rank = self.ranker.rank_hand(hand)
        return hand

    def size(self):
        return len(self.cards)
