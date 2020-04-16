"""
Data Types for Cards
"""

import enum


class Suite(enum.Enum):
    SPADES = '♠'
    HEARTS = '♥'
    CLUBS = '♣'
    DIAMONDS = '♦'

    
class Rank(enum.Enum):
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'
    SIX = '6'
    SEVEN = '7'
    EIGHT = '8'
    NINE = '9'
    TEN = '10'    
    JACK = 'J'    
    QUEEN = 'Q'
    KING = 'K'
    ACE = 'A'