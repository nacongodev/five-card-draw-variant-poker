class Hand:
    def __init__(self, cards=None):
        if cards is None:
            cards = []
        self.cards = cards

    def add_card(self, card):
        self.cards.append(card)

    def __len__(self):
        return self.cards
