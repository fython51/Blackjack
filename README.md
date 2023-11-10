# Blackjack
This project is an implementation of Blackjack in python, completed for the Introduction to Programming course at Nova SBE. 

<br>

---

<br>
<br>

## The Project
This project aims at coding an online version of the BlackJack game on Python.

As in a casino, there are multiple players playing individually against the dealer. Specifically, in this example we have two players, Nicholas and Joel, playing against the dealer, Bianca. Both Nicholas and Joel have \\$1,000 to spend on this game, while Bianca has \\$100,000. We have only two players in the example to keep the output short and to the point, but many more can be added.

<br>

### Objective
The objective is to achieve an overall hand value of 21. Therefore, each round, the closer the player gets to this number, the riskier it is to choose hit and get another card. This is because if the hand value exceeds 21, the player is bust: the player loses its bet amount and the house wins. So, for instance, if a player reaches a total value of 17, if he/she is very risk averse, the player should choose to stay. After a player has chosen to stay or if they're bust, the game moves on to the second player, following the same process. Finally, after all the players have played, it is the dealer’s turn. If the dealer achieves a hand value higher than the players who have chosen to stay, but not greater than 21, the house wins. Otherwise, the non-busted player with the hand value closest to 21 wins. 

<br>

### How to Set Up the Game
1. The user(s) create a series of Player objects, determining their name and available money and whether they are the dealer or not. 
2. The player objects that **are not** dealers must be placed into a list, which is then passed as the **first** argument of the `play_blackjack()` function. 
3. The player object that **is** the dealer must be passed directly as the **second** argument of the function. 
4. The user(s) must then select how many decks to play with, inserting the integer number as the **third and final** argument of the function.


<br>

### The Rules
At the beginning, each player must decide an amount to bet. This amount must be an integer between 0 and the max amount of money each player has. That is, in this example, Nicholas and Joel can choose and amount between \\$0 and \\$1,000 inclusive. After having placed a bet, the dealer will give two cards to the first player. Then, based on the hand value (the sum of values of the 2 cards) and on the hand value of the dealer, the player must decide whether to hit or stay. That is, by choosing hit, the dealer will assign a new card to the player. He/she will then have to decide again whether to hit or stay based on the new hand value, unless they've already gone bust.

It is important to highlight how to count the values of each card. It is very simple: cards $K$, $Q$, and $J$ always have a value of 10; cards between 2 and 10 included are worth their face value. That is, 10 = 10, 9 = 9, and so on. An Ace's value is 11 unless this would cause the player to bust, in which case it becomes worth 1.

Before seeing the cards of the dealer and of themselves, the players place their bets. Then, after a first round is completed, i.e., all the players have played, the money will lose their money permanently if they lose or go bust, win their bets back in double if they win, and recoup their bet if there is a draw. For example, if in round one Nicholas places a bet of \\$300 and goes bust, in round two he can only bet an amount between \\$0 and \\$700 (\\$1,000 - \\$300). On the other hand, if he wins, he can now place a bet ranging from \\$0 and \\$1,300. 

After placing new bets, the game starts again. At the beginning of each round, a new deck is generated, which prevents card-counting cheating, and each player can decide whether to place their bet or to exit the game. 

<br>

### Code Structure
The code is based on classes and functions.

1. **Classes:** we created two classes, one for the cards and one for the players. Specifically, with the `Cards` class, we assigned a suit (hearts, flowers…), a name ($K$, $Q$…), and a value (1, 2…) to each card. We also created a method to print cards, showing their name and their suit. With the `Player` class, we added attributes such as the name, the amount of money available for playing, and the role (dealer or player) of each participant of Blackjack. Furthermore, we coded a set of methods that allow players to take specific actions during the game. These include, for example, giving a card to the player once choosing to hit (and running a series of checks on the card and the player thereafter), or resetting the hand once the round is complete.
2. **Functions:** we created a set of functions to run the game. For example: one generates the decks of cards, one shuffles said decks, and one shows the hands of all the players.

The use of classes made our _building-in-small-steps_ approach to coding this programme possible. We initially coded a single hand, without money or a dealer, then we added both, one after the other, then we added a method to print cards with a design we could easily change and update, etc. 

For the deck, instead of creating a local variable that was returned in multiple functions, we decided to have a function, `generate_deck()`, create a global variable, which then allows other functions and methods to interact with the deck without it having to be passed as an argument. The advantage for us to employ the use of a global variable, of course, is that coding the interactions with the deck is simpler.

The game also makes extensive use of `while` loops, not only to actually run itself, but to keep user inputs under control.

<br>

### User Inputs
In any scenario where there are user inputs, they have to be controlled in order to avoid errors and manipulation. We have users use inputs at several points in the game:
- To choose whether to make a bet or exit;
- To choose the amount to bet;
- To choose whether to hit or stay.

In each situation, checks have been put in place to avoid users selecting invalid inputs. We have also added a check that ensures that no dealer is slipped into the list of players, and we used type hints in our `play_blackjack` function, so as to avoid an incorrect setup of the game in the first place.

<br>

### Our Value Added
There are many python blackjack simulators available online, with each offering unique charateristics. The unique characteristic of ours is that it allows for multiple players to play against the dealer – all of the solutions we found online were solitary games.

Additionally, we have a unique card design, although it was inspired by [AskPython's blackjack game.](https://www.askpython.com/python/examples/blackjack-game-using-python) This version also confirmed our intention to use classes for the cards, although we took this one step further, and used classes for the players (and dealer) as well. Conversely, we liked [the approach of github user _marcosan93_](https://github.com/marcosan93/Blackjack-Card-Counter-Simulator) to use several small functions (in our case also small methods), which allowed us to de-clutter the code and make any de-bugging easier.

Lastly, neither of these two examples took the pace of the game into account. We, on the other hand, decided to make the game run at a more "human" pace by employing the use of `time.sleep(1)` at several points in the game. We found that otherwise the game had a very robotic, "rushed" feel.

<br>
<br>

