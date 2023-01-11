from collections import Counter
class Ranker:
    def __init__(self):
        pass

    def rank_hand(self, hand):
        hand_rank = self.evaluate_hand(hand)
        return hand_rank

    def evaluate_hand(self, hand):
        if self.is_straight_flush(hand):
            return "Straight Flush"
        elif self.is_four_of_a_kind(hand):
            return "Four of a Kind"
        elif self.is_full_house(hand):
            return "Full House"
        elif self.is_flush(hand):
            return "Flush"
        elif self.is_straight(hand):
            return "Straight"
        elif self.is_three_of_a_kind(hand):
            return "Three of a Kind"
        elif self.is_two_pair(hand):
            return "Two Pair"
        elif self.is_pair(hand):
            return "One Pair"
        else:
            return "High Cards"

    def is_straight_flush(self, hand):
        sorted_hand = sorted(hand, key=lambda x: x.rank)
        if self.is_flush(hand) and self.is_straight(sorted_hand):
            return True
        return False

    def is_four_of_a_kind(self, hand):
        rank_counts = Counter(card.rank for card in hand)
        for count in rank_counts.values():
            if count == 4:
                return True
        return False

    def is_full_house(self, hand):
        rank_counts = Counter(card.rank for card in hand)
        three_of_a_kind = False
        two_of_a_kind = False
        for count in rank_counts.values():
            if count == 3:
                three_of_a_kind = True
            elif count == 2:
                two_of_a_kind = True
        return three_of_a_kind and two_of_a_kind

    def is_flush(self, hand):
        suit_counts = Counter(card.suit for card in hand)
        for count in suit_counts.values():
            if count == 5:
                return True
        return False

    def is_straight(self, hand):
        ranks = [card.rank for card in hand]
        ranks_set = set(ranks)
        if len(ranks_set) != 5:
            return False
        if max(ranks_set) - min(ranks_set) == 4:
            return True
        if ranks == [14, 2, 3, 4, 5]:
            return True
        return False

    def is_three_of_a_kind(self, hand):
        rank_counts = Counter(card.rank for card in hand)
        for count in rank_counts.values():
            if count == 3:
                return True
        return False

    def is_two_pair(self, hand):
        rank_counts = Counter(card.rank for card in hand)
        num_pairs = 0
        for count in rank_counts.values():
            if count == 2:
                num_pairs += 1
        return num_pairs == 2

    def is_pair(self, hand):
        rank_counts = Counter(card.rank for card in hand)
        for count in rank_counts.values():
            if count == 2:
                return True
        return False
