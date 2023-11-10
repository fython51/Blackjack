#######################################
# Setup
#######################################
# Import packages #####################
import random
import time

# Classes #############################
class Card:
    def __init__(self, suit, name, value):
        self.suit = suit
        self.name = name
        self.value = value
    
    def print_card(self):
        """
        Print the card: show its suit and the name.
        """
        if self.name != 10:
            print(f"""
                |{self.suit}   |
                |    |
                |   {self.name}|
                """)
        else:
            print(f"""
                |{self.suit}   |
                |    |
                | {self.name}|
                """)

        
class Player:
    def __init__(self, name, money, is_dealer = False):
        self.is_dealer = is_dealer
        if is_dealer:
            self.name = name
            self.money = money
        else:
            self.name = name
            self.money = money 
        self.reset_hand()

    def reset_hand(self):
        """
        Reset the hand: empty the list of cards in the hand, reset the hand value to 0, and reset the `is_bust` status.
        """
        self.hand = []
        self.value = 0
        self.is_bust = False
    
    def hit(self):
        """
        Hit the player: pop a card from the deck, append it to the player's hand, adjust the hand value if the card is an ace, 
        and adjust the `is_bust` status if necessary. 
        """
        card = deck.pop()
        self.hand.append(card)
        self.ace_check(card)
        self.value += card.value         
        self.bust_check()

    def bust_check(self):
        if self.value > 21:
            self.is_bust = True
            print(f"{self.name}, you're bust!")
            if not self.is_dealer:
                self.show_hand()
# checks if the card is an Ace, as the card has a specific value in Blackjack.
    def ace_check(self, card):
        if card.name == "A":
            if self.value > 10: 
                self.value -= 10
# This function is used to print out a persons current card value. It also hides the dealers first, as is the rules of Blackjack.
    def show_hand(self):
        if self.is_dealer:
            if self.is_bust:
                print(f"Hand value: {self.value}")
                for card in self.hand: 
                    card.print_card()    
            else: 
                for card_no, card in enumerate(self.hand): 
                    if card_no == 0:
                        print("(Hidden first card)")
                    else:
                        card.print_card()
        else:
            print(f"{self.name}'s hand value: {self.value}")
            for card in self.hand: 
                card.print_card()
        print()
                
    def show_all(self):
        print(f"{self.name}'s hand value: {self.value}")
        for card in self.hand: 
            card.print_card()
        print()
   
    def bet(self, amount):
        self.money -= amount
        
    def receive(self, amount): 
        self.money += amount 


# Functions ###########################
def generate_deck(no_of_decks = 2):
    # Define the parameters
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
    suit_icons = {"Spades":"\u2664", "Hearts":"\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    card_values = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}

    # Generate the deck
    global deck
    deck = [Card(suit_icons[suit], card, card_values[card]) for card in cards for suit in suits]
    deck *= (4 * no_of_decks)
    
    
def shuffle_deck():
    random.shuffle(deck)

# Deals out the card until every player has 2 cards.
def deal_cards(players_list):
    for player in players_list:
        player.reset_hand()
        while len(player.hand) < 2:
            player.hit()


def show_hands(players_list):
    for player in players_list:
        player.show_hand()


def check_for_dealer(players_list):
    for player in players_list:
        if player.is_dealer:
            print(f"{player.name} appears to be a dealer! Please select only one dealer and insert them in the `dealer` parameter only.")
            return True
        else:
            return False


#######################################
# The game
#######################################
def play_blackjack(players_list: list, dealer: Player, no_of_decks: int):
    dict_bets = {}
    generate_deck(no_of_decks)             
    shuffle_deck()
    playing_players = []
    possible_responses = ["hit", "h", "stay", "s"]
    possible_responses_exit = ["exit","e"]
    possible_responses_bet = ["bet","b"]
   
    if check_for_dealer(players_list):
        return
#gives the players_list[index] bet or exit option, also checks for wrong inputs.
    index = 0
    while index != len(players_list):
        dict_bets[players_list[index]] = 0
        bet_exit = input(f"{players_list[index].name}, would you like to Bet or Exit?")
        bet_exit = bet_exit.strip().lower()

        if bet_exit in possible_responses_exit:
            print(f"{players_list[index].name} left the table!")
            index += 1
            
               
        elif bet_exit in possible_responses_bet:
            
            bet_value = None
            while True:
                bet_value = input(f"{players_list[index].name}, place your bet: ")          
                try:
                    bet_value = int(bet_value)

                    if bet_value <= 0:
                        print(f"{players_list[index].name}, that number is negative.")
                        continue
                except:
                    print(f"Sorry, that is not a valid bet amount. It has to be a number lower than {players_list[index].money}")
                    continue
                if players_list[index].money >= bet_value: 
                    dict_bets[players_list[index]] += bet_value
                    players_list[index].bet(bet_value)
                    playing_players.append(players_list[index])
                    index += 1
                elif players_list[index].money == 0:
                    print(f"{players_list[index].name}, you've run out of money. You will be kicked out of the table.")
                    index += 1
                else: 
                    print(f"{players_list[index].name}, you only have {players_list[index].money} to bet, choose something else.")
                    continue 
                break
        else:
            print("Thats not a valid option. Please write bet or exit.")    
    if len(playing_players) == 0:
        print("All players have left the table! Thank you for playing.")
        return
    deal_cards(playing_players)
    deal_cards([dealer])
    print(f"\n{dealer.name}'s hand:")
    dealer.show_hand()

    # The game is played
    for player in playing_players:
        while not player.is_bust:
            
            time.sleep(1)
            player.show_hand()

            action = input(f"\n{player.name},Would you like to hit or stay? ")
            action = action.strip().lower()
            if action in possible_responses[:2]:
                player.hit()
            elif action in possible_responses[2:4]:
                break
            else:
                while action not in possible_responses:
                    action = input("Incorrect input. Would you like to hit or stay?")


    print(f"\n{dealer.name} is playing.\n")
    while dealer.value <= 17:
        time.sleep(1)
        dealer.hit()
        dealer.show_hand()

    if not dealer.is_bust:
        time.sleep(1)
        dealer.show_all()

    for player in playing_players:
        
        time.sleep(1)
        
        if dealer.is_bust and not player.is_bust:
            print(f"{player.name}, you win.\n")
            player.receive(2*dict_bets[player])
            dealer.bet(dict_bets[player])

        elif dealer.is_bust and player.is_bust:
            print(f"{player.name}, it's a draw. Nobody wins.\n")
            player.receive(dict_bets[player])

        elif player.is_bust and not dealer.is_bust:
            print(f"{player.name}, the house wins.\n")
            dealer.receive(dict_bets[player])            

        else:
            if player.value > dealer.value:
                print(f"{player.name}, you win.\n")
                player.receive(2*dict_bets[player])
                dealer.bet(dict_bets[player])

            elif dealer.value > player.value:
                print(f"{player.name}, the house wins.\n")
                dealer.receive(dict_bets[player])

            else:
                print(f"{player.name}, it's a draw. Nobody wins.\n")
                player.receive(dict_bets[player])

    # Show stats
    time.sleep(1)
    print("Current stats:")
    for player in playing_players:
        print(f"{player.name}: {player.money:,d}")
    print(f"{dealer.name}: {dealer.money:,d}\n")

    # The hands are reset
    for player in playing_players:
        player.reset_hand()
    dealer.reset_hand()
    
    if len(playing_players) > 0: 
        play_blackjack(playing_players,dealer, no_of_decks)


#######################################
# Running the game
#######################################
Nicholas, Joel, Camilla, Bianca = Player("Nicholas", 1000),Player("Joel",1000), Player("Camilla", 2000), Player("Bianca", 100000, is_dealer = True)
players = [Nicholas, Joel, Camilla]
dealer = Bianca

play_blackjack(players, dealer, 
               no_of_decks = 2)
