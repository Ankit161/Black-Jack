#Game of Black Jack
import random

#from IPython.display import clear_output
#To use clear_output(), Replace all: print('\n'*100) with clear_output()

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

# Creating Card 
class Card:
    
    # Creating Card 
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank +" of " + self.suit
    
#Creating a deck of cards
class Deck:
    
    def __init__(self):
        self.all_cards = []
        
     #creating a deck of cards   
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit,rank))
                
     #Shuffle the deck of cards at random           
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    #remove last card and return it 
    def hit(self):
        return self.all_cards.pop()
    
    #remove last card and return it
    def deal(self):
        return self.all_cards.pop()

#Creating a class for Account
class Account:
    #Account holder name and balance passed as argument
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    
    # Shows account holder name and balance when used in print function
    def __str__(self):
        return(f"Name:  = {self.name}\nBalance:  = {self.balance}")
    
    #Substracts the betted amount from the current balance and return new balance amount.           
    def bet_lost(self,bet_amount):
        self.balance -= bet_amount
        
        #sets betted amount back to 0
        bet = 0
        return f'{self.balance} Left'
    
    #Adds the betted amount to the current balance and return new balance amount
    def bet_won(self,bet_amount):
        self.balance += bet_amount
        
        #sets betted amount back to 0
        bet = 0
        return f'{self.balance} Left'
        
#Creating a start game Function
def start_game():
    while True:
        #player inputs for starting the game.
        player_start = input("Start Game of Black Jack(Y or N)! ").upper()

         # Counter against wrong input
        if player_start != '':
            
            #if Yes than return true and break from the while loop
            if player_start[0] == 'Y':
                return True
                break

            #if NO than return False and break from the while loop
            elif player_start[0] == 'N':
                return False
                break
            else:
                print('Please Enter Y or N')
        else:
            print('Please Enter Y or N')

#Creating a replay game Function
def replay_game():
    
    while True:
        #player inputs for Replaying the game.
        player_start = input("Replay (Y or N)! ").upper()
        
        # Counter against wrong input
        if player_start != '':
            
            #if Yes than return true and break from the while loop
            if player_start[0] == 'Y':
                return True
                break

            #if NO than return False and break from the while loop
            elif player_start[0] == 'N':
                return False
                break
                
            # Counter against wrong input
            else:
                print('Please Enter Y or N')
        # Counter against wrong input        
        else:
            print('Please Enter Y or N')

#Creating a player account detail Function using Class Account
def player_acc_int():
    #Creating a black player account list
    player_detail = []
    
    #Taking input for account holder name.
    player_name = input('Please Enter your Name! ')
    
    #Attaching holder name to empty player detail list.
    player_detail.append(player_name)
    
    #Taking input for account holder balance.
    player_amount = int(input('Please Enter your Amount! '))
    
    #Attaching balance to empty player detail list.
    player_detail.append(player_amount)
    
    #Aeturning Account holder details
    return player_detail

#Creating Players Input for hit or Stay
def player_int():
    while True:

        #Taking input from player for Hit or stay.
        player_start = input("Hit or Stay (H or S)! ").upper()
        
        # Counter against wrong input
        if player_start != '':
            
            #if Yes than return true and break from the while loop
            if player_start[0] == 'H':
                return True
                break

            #if NO than return False and break from the while loop
            elif player_start[0] == 'S':
                return False
                break
                
            # Counter against wrong input
            else:
                print('Please Enter Hit or Stay')
        # Counter against wrong input        
        else:
            print('Please Enter Hit or Stay')

#Displaying the Output
def display(winner = '',player_sum = 0 ,dealer_sum = 0,player_account = 0,player_bet = 0):
    
    #displays the Sums of dealer.
    print(f'Dealer-total-sum-| {dealer_sum} |')
    
    #displays the winner of the round.
    print(f'------{winner}------')
    
    #displays the Sums of dealer.
    print(f'Player-total-sum-| {player_sum} |')
    
    #displays players bet    
    print(f'bet={player_bet}')

#Taking Input from the player for starting the game.
print('\n'*100)
game_on = start_game()
    
while game_on:
        
        print('\n'*100)
        
        #Taking players detail
        player_detail = player_acc_int()
        
        #Creating Account of Player Using Account CLass
        player_account = Account(player_detail[0],player_detail[1])
        
        #counter to control game replay.
        deal_on = True
        
        while deal_on:
            #clear Display 
            print('\n'*100)
            
            #Creating VAriable and lists required for game.
            player_sum = 0
            dealer_sum = 0
            player_bet =  0
            player_cards = []
            dealer_cards = []
            winner = ''
            
            #Pre-condition for game
            
            winner_state = False
            player_input = True
            bet_able = True
            
            
            #Creating a Deck of Cards
            cards_deck = Deck()
            
            #shuffling the deck of Cards
            cards_deck.shuffle()

            #to check if random and shuffle are working uncomment below line
            #print(cards_deck.all_cards[0])
            
            #Display Player balance available.
            print(f'Amount {player_account.balance} Available')
            
            while bet_able:
                
                #Input player bet.
                player_bet = int(input('Place your bet! '))
                
                #check player bet amount with balance
                if player_bet<=player_account.balance:
                    bet_able = False
                    
                #message for false bet amount
                else:
                    print('Not Enough Fund Available')
            
            #Distributing Cards to Player and Dealer list.
            for i in range(1,3):
                player_cards.append(cards_deck.deal())
                dealer_cards.append(cards_deck.deal())
             
            #Calculating Sum of ALL Cards in Player's hand.
            for i in range(len(player_cards)):
                player_sum += player_cards[i].value
                
            #Calculating Sum of only first Cards in Dealer's hand.   
            dealer_sum = dealer_cards[0].value
            
            print('\n'*100)
            #Displaying the sum of Player's and Dealer's Hand.
            display(winner,player_sum,dealer_sum,player_account,player_bet)
            
            #Condition to checking if player has two Aces.
            if player_sum >21:
                
                #Converting One of the Aces value from 11 to  1.
                player_cards[0].value = 1
                
                #Re-calculating the sum of Player's hand.
                for i in range(len(player_cards)):
                    player_sum += player_cards[i].value
                
            #Check if Player's hand is Black jack and declare player as winner.     
            elif player_sum == 21:
                print('\n'*100)
                winner = 'PLAYER  WINS'
                display(winner,player_sum,dealer_sum,player_account,player_bet)
                #print('Black Jack for Player!')
                player_account.bet_won(player_bet)
                winner_state = True
                
            else:
                pass
                        
            while winner_state == False and player_input == True:
                #Taking input from player for hit or stay.
                player_input = player_int()
                
                #Adding A card into player hand as player wants to hit.
                if player_input:
                    
                    print('\n'*100)
                    
                    #adding card to players hand.
                    player_sum += player_cards[-1].value
                    
                    #recalculating sum of player hand
                    display(winner,player_sum,dealer_sum,player_account,player_bet)
                    
                    #Check winner 
                    if player_sum >21:
                        print('\n'*100)
                        winner = 'DEALER  WINS, Player Busted'
                        display(winner,player_sum,dealer_sum,player_account,player_bet)
                        
                        #Substracting bet from players balance
                        player_account.bet_lost(player_bet)
                        winner_state = True
                    
                    elif player_sum == 21:
                        print('\n'*100)
                        winner = 'PLAYER  WINS'
                        display(winner,player_sum,dealer_sum,player_account,player_bet)
                        
                        #Adding won bet into players balance
                        player_account.bet_won(player_bet)
                        winner_state = True

                    else:
                        pass
                else:
                    pass
                
            if player_input == False and winner_state == False:
                #adding dealers second card onn hand to sum value
                dealer_sum += dealer_cards[-1].value
            
                #checking if both cards are Aces
                if dealer_sum > 21:
                    #Converting One of the two Aces value from 11 to  1.
                    dealer_cards[0].value = 1
                
                    #Re-calculating the sum of Player's hand.
                    for i in range(len(dealer_cards)):
                        dealer_sum += dealer_cards[i].value
                else:
                    pass
            else:
                pass            
            
    #Dealer Turn
            while player_input == False and winner_state == False:
                
                # Check if dealer busted or not                  
                if dealer_sum >21:
                    
                        #check if dealer's new card in hand is Ace and if Ace convert it value from 11 to 1.
                        if dealer_cards[-1].value == 11:
                            dealer_cards[-1].value = 1
                            
                            #Re-calculating the sum of Player's hand.
                            for i in range(len(dealer_cards)):
                                dealer_sum += dealer_cards[i].value
                            
                        else:
                            winner = 'PLAYER  WINS, Dealer Busted'
                            print('\n'*100)
                            display(winner,player_sum,dealer_sum,player_account,player_bet)
                    
                            #Adding won bet into players balance
                            player_account.bet_won(player_bet)
                            winner_state = True
                    
                
                #Add card to dealer hand if dealer's sum is less than player's sum.
                elif dealer_sum <= player_sum :
                        dealer_cards.append(cards_deck.hit())
                        dealer_sum += dealer_cards[-1].value
                        
                #Check if delaer's sum is greater than player's sum and not busted.       
                elif player_sum < dealer_sum <= 21:
                    print('\n'*100)
                    winner = 'DEALER  WINS'
                    display(winner,player_sum,dealer_sum,player_account,player_bet)
                    
                    #Substracting bet from players balance
                    player_account.bet_lost(player_bet)
                    winner_state = True
                    
     
                else:
                    pass 
                
            if player_account.balance == 0:
                print('No Amount left! Game Over')
                game_on == False
                break
            else:
                pass
            
            print(f'Amount {player_account.balance} Available')
            
            replay = replay_game()
            if replay == True:
                pass
            else:
                game_on = False
                break
        break               