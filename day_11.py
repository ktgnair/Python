# BlackJack Project

# Our Blackjack House Rules
# 1. The deck is unlimited in size. 
# 2. There are no jokers. The Jack/Queen/King all count as 10. The the Ace can count as 11 or 1.
# 3. Use the following list as the deck of cards: cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  
# 4. The cards in the list have equal probability of being drawn.
# 5. Cards are not removed from the deck as they are drawn.
# 6. The computer is the dealer.

from black_jack_ASCII import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Print final card list
def final_list_print(p_card, p_total, c_card, c_total):
   print(f"Your final hand: {p_card}, final score: {p_total}")
   print(f"Computer's final hand: {c_card}, final score: {c_total}")

# Check the total scores for player and computer
def find_total(total_score_cards):
   total = 0
   for i in range(len(total_score_cards)):
      total += total_score_cards[i]
   return total

# Checking conditions if player asks for another card
def checking_for_another_card_conditions(p_total, p_card, c_card, c_total):
   if p_total > 21:
      if 11 in p_card:
         index_of_value_change = p_card.index(11)
         p_card[index_of_value_change] = 1
         p_total = find_total(p_card)
         print(p_total)
         p_total = checking_for_another_card_conditions(p_total,p_card, c_card, c_total)
         return p_total
      else:
         final_list_print(p_card, p_total, c_card, c_total)
         print("You went over. You lose 😤")
         new_game()
   elif p_total < 21:
      return p_total
   else:
      final_list_print(p_card, p_total, c_card, c_total)
      print("Congrats!! You have got a BlackJack")
      new_game()

# Checking computer's 17 score condition
def checking_computer_conditions(c_total, c_card):
   if c_total < 17:
      c_card.append(random.choice(cards))
      c_total = find_total(c_card)
      checking_computer_conditions(c_total, c_card)
      return c_total
   else:
      c_total = find_total(c_card)
      return c_total

# The Begins Here
def new_game():
   start_game = input("Do you want to play the Black Jack Game. Press 'Y' if yes  else press 'N'! ").lower()
   if start_game == 'n':
      print("Thanks for playing the Game.")
      quit()
   elif start_game == 'y':
      print(logo)
      player_cards = random.sample(cards,2)
      player_total = find_total(player_cards)

      computer_cards = random.sample(cards,2)
      computer_total = find_total(computer_cards)
      
      print(f"Your cards are {player_cards}, current score is {player_total}")
      print(f"Computer's first card: {computer_cards[0]}")

      flag = True
      while flag:
         player_total = checking_for_another_card_conditions(player_total, player_cards, computer_cards, computer_total)
         next_round = input("Type 'y' to get another card, type 'n' to pass: ").lower()
         if next_round == "y":
            player_cards.append(random.choice(cards))
            player_total = find_total(player_cards)
            print(f"Your cards are {player_cards}, current score is {player_total}")
            print(f"Computer's first card: {computer_cards[0]}")
         else:
            flag = False
            if player_total < 21:
               computer_total = checking_computer_conditions(computer_total, computer_cards)
               if player_total > computer_total:
                  final_list_print(player_cards, player_total, computer_cards, computer_total)
                  print("You have won the game!!")
                  new_game()
               elif player_total < computer_total:
                  final_list_print(player_cards, player_total, computer_cards, computer_total)
                  print("You have lost the game!!")
                  new_game()    
            elif player_total == computer_total:
               final_list_print(player_cards, player_total, computer_cards, computer_total)
               print("This game is a Draw")
               new_game()
            else:
               final_list_print(player_cards, player_total, computer_cards, computer_total)
               print("Computer Won the Game")
               new_game()
   else:
      print("Please enter a valid input")
      new_game()
new_game()