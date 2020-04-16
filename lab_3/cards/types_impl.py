class Card:
    """
    ♠ ♥ ♦ ♣ 
    Value class representing a simple playing card from a 52 piece set
    """
    
    def __init__(self, card_string):
        self.suite, self.rank = card_string.split()

    def __repr__(self):
        return f'Card(rank="{self.rank}", suite="{self.suite}")'
    
    def __str__(self):
        return f'{self.rank}{self.suite}'
    
    def __iter__(self):
        return iter((self.rank, self.suite))  
    
    @property
    def score(self):
        if self.rank in (Rank.JACK.value, Rank.QUEEN.value, Rank.KING.value):
            result = '10'
        elif self.rank == Rank.ACE.value:
            result = '1/11'
        else:
            result = self.rank
        return result
        
    @staticmethod
    def combinations():
        return [
            Card(f'{suite.value} {rank.value}')
            for rank in Rank
            for suite in Suite
        ]


class Combo:
    def __init__(self, *cards):
        self.cards = cards
        
    def __add__(self, other):
        cards = self.cards + (other, )
        return Combo(*cards)
        
    def __repr__(self):
        return repr(self.cards)
    
    def _add(self, left, right):
        if left == '' or right == '':
            return left or right
 
        if '/' not in left and '/' not in right:
            return f'{int(left) + int(right)}'
        
        if '/' in left and '/' not in right:
            min_left, max_left = left.split('/')
            return f'{int(min_left) + int(right)}/{int(max_left) + int(right)}'
    
    @property
    def score(self):
        """
        9 + 2 = 11
        1/11 + 2 = 3/13
        1/11 + 1/11 = 2/12/22 -> 2/12
        1/11 + 1/11 + 1/11 = 3/13/23/33 -> 3/13
        1/11 + 1/11 + 1/11 + 1/11 = 4/14/24/34/44 -> 4/14
        1/11 + K = 21
        """
        
        result = ''
        for card in self.cards:
            result = self._add(result, card.score)
        return result

for i in Card('♣ 10'):
    print (i)
    
for card in Card.combinations()[:5]:
    print (card, card.score)
    
# Card('♣ 10') + Card('♦ A')
pair = Combo() + Card('♦ K') + Card('♣ A')
pair2 = Combo() + Card('♦ 2') + Card('♣ A') + Card('♦ A')

print('score', pair.score)
print('score', pair2.score)