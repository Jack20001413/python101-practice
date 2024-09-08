class Card:
    def __init__(self, suit, rank) -> None:
        self.suit = suit
        self.rank = rank
    
    def __str__(self) -> str:
        return f"{self.rank['rank']} of {self.suit}"