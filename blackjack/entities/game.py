from .hand import Hand
from .deck import Deck


class Game:
    def play(self):
        game_number = 0
        games_to_play = 0

        while games_to_play <= 0:
            try:
                game_to_play = int(input("How many games do you want to play?"))
            except:
                print("You must enter a number.")
        
        while game_number < games_to_play:
            game_number += 1

            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(dealer=True)

            for i in range(2):
                player_hand.add_card(deck.deal())
                dealer_hand.add_card(deck.deal())

            print()
            print("*" * 30)
            print(f"Game {game_number} of {games_to_play}")
            player_hand.display()
            dealer_hand.display()

        def check_winner(self, player_hand, dealer_hand):
            if player_hand.get_value() > 21:
                print("You busted. Dealer wins!😊")
                return True
            elif dealer_hand.get_value() > 21:
                print("You busted. You wins!😊")
                return True
            elif dealer_hand.is_blackjack() and player_hand.is_blackjack():
                print("Both of you have blackjack! Tie!")
            elif player_hand.is_blackjack():
                print("You have blackjack. You win!")
            return False