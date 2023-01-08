class Ranker:
    def __init__(self):
        self.ranks = ['high card', 'pair', 'two pair', 'three of a kind', 'straight', 'flush', 'full house',
                      'four of a kind', 'straight flush']

    def rank_hand(self, hand):
        ranks = []
        for card in hand.cards:
            ranks.append(card.rank)

        if self.is_straight_flush(hand):
            return self.ranks[8]
        elif self.is_four_of_a_kind(hand):
            return self.ranks[7]
        elif self.is_full_house(hand):
            return self.ranks[6]
        elif self.is_flush(hand):
            return self.ranks[5]
        elif self.is_straight(hand):
            return self.ranks[4]
        elif self.is_three_of_a_kind(hand):
            return self.ranks[3]
        elif self.is_two_pair(hand):
            return self.ranks[2]
        elif self.is_pair(hand):
            return self.ranks[1]
        else:
            return self.ranks[0]

    def is_pair(self, hand):
        ranks = []
        for card in hand.cards:
            ranks.append(card.rank)
        return len(set(ranks)) == 4

    def is_two_pair(self, hand):
        ranks = []
        for card in hand.cards:
            ranks.append(card.rank)
        return len(set(ranks)) == 3

    def is_three_of_a_kind(self, hand):
        ranks = []
        for card in hand.cards:
            ranks.append(card.rank)
        return len(set(ranks)) == 3

    def is_straight(self, hand):
        ranks = []
        for card in hand.cards:
            ranks.append(card.rank)
        ranks.sort()
        return ranks[-1] - ranks[0] == 4

    def is_flush(self, hand):
        suits = []
        for card in hand.cards:
            suits.append(card.suit)
        return len(set(suits)) == 1

    def is_full_house(self, hand):
        ranks = []
        for card in hand.cards:
            ranks.append(card.rank)
        return len(set(ranks)) == 2

    def is_four_of_a_kind(self, hand):
        ranks = []
        for card in hand.cards:
            ranks.append(card.rank)
        return len(set(ranks)) == 2

    def is_straight_flush(self, hand):
        return self.is_straight(hand) and self.is_flush(hand)
