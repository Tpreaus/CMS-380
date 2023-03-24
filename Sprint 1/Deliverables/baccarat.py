"""
Theodore Preaus CMS-380

Create a program to simulate the odds for winning in
a game of baccarat for player and dealer hands 

"""
from random import randint

def simulate():
  """
  Simulate one round of Baccarat
  """
  # Create the possible results
  # Player wins = 0
  # Dealer wins = 1
  # Tie = 2
  
  # Create the shoe
  shoe = []
  for deck in range(8):
    for Aces in range(4):
      shoe.append(1)
    for twos in range(4):
      shoe.append(2)
    for threes in range(4):
      shoe.append(3)
    for fours in range(4):
      shoe.append(4)
    for fives in range(4):
      shoe.append(5)
    for six in range(4):
      shoe.append(6)
    for seven in range(4):
      shoe.append(7)
    for eight in range(4):
      shoe.append(8)
    for nines in range(4):
      shoe.append(9)
    for tens_and_face in range(16):
      shoe.append(10)

  # Deal cards to the player
  player_cards = []
  dealer_cards = []
  player_cards.append(shoe[randint(1, 415)])
  dealer_cards.append(shoe[randint(1, 415)])
  player_cards.append(shoe[randint(1, 415)])
  dealer_cards.append(shoe[randint(1, 415)])

  player_first_check = sum(player_cards) % 10
  dealer_first_check = sum(dealer_cards) % 10
  # Check for naturals 
  if(player_first_check >= 8):
    if(dealer_first_check >= 8):
      if (player_first_check > dealer_first_check):
        # Player wins Natural 9 over 8
        return 0
      if (player_first_check == dealer_first_check):
        # Bets push returns tie
        return 2
      # Dealer wins 9 over 8
      return 1
    # Player Wins on Natural
    return 0
  if(dealer_first_check >= 8):
    # Dealer wins on natual 
    return 1

  # At this point both hands have no naturals 
  # if player hand is less than 6 hit
  if(player_first_check <= 5):
    player_cards.append(shoe[randint(0, 415)])
    player_second_check = sum(player_cards) % 10
    #Check if banker will hit
    if (dealer_first_check <= 2):
      dealer_cards.append(shoe[randint(1, 415)])
      dealer_second_check = sum(dealer_cards) % 10
      # check to see who won with three cards
      if (dealer_second_check == player_second_check):
        #return tie 
        return 2
      if (dealer_second_check > player_second_check):
        # dealer wins
        return 1
      if (dealer_second_check < player_second_check):
        #player wins
        return 0
    if (dealer_first_check == 7):
      if (player_second_check == 7):
        #return tie on 7
        return 2
      if (player_second_check > dealer_first_check):
        # player wins
        return 0
      # Dealer wins with 7
      return 1
    # Check for 6
    if (dealer_first_check == 6):
      #check player hand for 6 or 7 and draw
      if (player_second_check == 6):
        dealer_cards.append(shoe[randint(0, 415)])
        dealer_second_check = sum(dealer_cards) % 10
        if (dealer_second_check == player_second_check):
          #return tie 
          return 2
        if (dealer_second_check > player_second_check):
          # dealer wins
          return 1
        if (dealer_second_check < player_second_check):
          #player wins
          return 0
      if (player_second_check == 7):
        dealer_cards.append(shoe[randint(0, 415)])
        dealer_second_check = sum(dealer_cards) % 10
        if (dealer_second_check == player_second_check):
          #return tie 
          return 2
        if (dealer_second_check > player_second_check):
          # dealer wins
          return 1
        if (dealer_second_check < player_second_check):
          #player wins
          return 0
      if (dealer_first_check == player_second_check):
        #return tie
        return 2
      if (dealer_first_check > player_second_check):
        #dealer wins
        return 1
      if (dealer_first_check < player_second_check):
        #player wins
        return 0
    if (dealer_first_check == 5):
      if (player_second_check < 4):
        # Dealer win
        return 1
      if (player_second_check < 8):
        dealer_cards.append(shoe[randint(0, 415)])
        dealer_second_check = sum(dealer_cards) % 10
        # Check third card
        if (dealer_second_check == player_second_check):
          #return tie 
          return 2
        if (dealer_second_check > player_second_check):
          # dealer wins
          return 1
        if (dealer_second_check < player_second_check):
          #player wins
          return 0
      if (player_second_check > 7):
        #player wins
        return 0
    if (dealer_first_check == 4):
      if (player_second_check < 2):
        #dealer wins 
        return 1
      if (player_second_check < 8):
        dealer_cards.append(shoe[randint(0, 415)])
        dealer_second_check = sum(dealer_cards) % 10
        # Check third card
        if (dealer_second_check == player_second_check):
          #return tie 
          return 2
        if (dealer_second_check > player_second_check):
          # dealer wins
          return 1
        if (dealer_second_check < player_second_check):
          #player wins
          return 0
      if (player_second_check > 7):
        #player wins
        return 0
    if (dealer_first_check == 3):
      if (player_second_check < 8):
        dealer_cards.append(shoe[randint(0, 415)])
        dealer_second_check = sum(dealer_cards) % 10
        # Check third card
        if (dealer_second_check == player_second_check):
          #return tie 
          return 2
        if (dealer_second_check > player_second_check):
          # dealer wins
          return 1
        if (dealer_second_check < player_second_check):
          #player wins
          return 0
      if (player_second_check == 8):
        #player wins
        return 0
      if (player_second_check == 9):
        dealer_cards.append(shoe[randint(0, 415)])
        dealer_second_check = sum(dealer_cards) % 10
        # Check third card
        if (dealer_second_check == player_second_check):
          #return tie 
          return 2
        if (dealer_second_check > player_second_check):
          # dealer wins
          return 1
        if (dealer_second_check < player_second_check):
          #player wins
          return 0
  # player hand 6 or 7 and dealer hit
  if(dealer_first_check <= 5):
    dealer_cards.append(shoe[randint(0, 415)])
    dealer_final_check = sum(dealer_cards) % 10
    if (dealer_final_check == player_first_check):
      #tie
      return 2
    if (dealer_final_check > player_first_check):
      #dealer win
      return 1
    if (player_first_check > dealer_final_check):
      #player win
      return 0



###### Main

num_trials = 100000
num_player_wins = 0
num_dealer_wins = 0
num_ties = 0

for trial in range(num_trials):
  win = simulate()
  if (win == 0):
    num_player_wins += 1
  if (win == 1):
    num_dealer_wins += 1
  if (win == 2):
    num_ties += 1

frac_player = num_player_wins / num_trials
frac_deal = num_dealer_wins / num_trials
frac_tie = num_ties / num_trials

print("Fraction of player wins:", frac_player)
print("Fraction of dealer wins:", frac_deal)
print("Fraction of tie:", frac_tie)

house_edge = (frac_player * 1) + (frac_deal * -1) + (frac_tie * 0)
print("House Edge", house_edge)
