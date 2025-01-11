import random
from art import logo

# Function to deal a card to the player or computer
def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

# Function to calculate the total score of the hand
def calculate_score(hand):
    """Calculates the score based on the hand, adjusting for Aces (11)"""
    score = sum(hand)

    # Adjust for Aces (11) if the score is over 21
    ace_count = hand.count(11)
    while score > 21 and ace_count:
        score -= 10  # Adjust one Ace from 11 to 1
        ace_count -= 1

    return score

# Function to play the game
def play_game():
    """Plays a single game of Blackjack"""
    print(logo)
    player = []
    computer = []

    # Deal initial two cards to player and computer
    for _ in range(2):
        player.append(deal_card())
        computer.append(deal_card())

    # Calculate initial scores
    player_score = calculate_score(player)
    computer_score = calculate_score(computer)

    # Show initial hands and scores
    print(f"Your cards: {player}, current score: {player_score}")
    print(f"Computer's first card: {computer[0]}")

    # Player's turn
    while player_score < 21:
        draw_a_card = input("Do you want to draw another card? Type 'y' to draw, 'n' to pass: ")
        if draw_a_card == "y":
            player.append(deal_card())
            player_score = calculate_score(player)
            print(f"Your cards: {player}, current score: {player_score}")
        elif draw_a_card == "n":
            break

    # Computer's turn: draws cards until score is at least 17
    while computer_score < 17:
        computer.append(deal_card())
        computer_score = calculate_score(computer)

    # Final hands and scores
    print(f"Your final hand: {player}, final score: {player_score}")
    print(f"Computer's final hand: {computer}, final score: {computer_score}")

    # Determine the outcome
    if player_score > 21:
        print("BUST! You lose 😭")
    elif computer_score > 21:
        print("Computer BUST! You win 😁")
    elif player_score > computer_score:
        print("You win 😃")
    elif player_score < computer_score:
        print("Computer wins 😤")
    else:
        print("It's a draw 🙃")

# Main game loop
def main():
    """Main function to start and play the Blackjack game"""
    play_more = input("Do you want to play a game of Blackjack? Type 'y' or 'n':\n ")
    while play_more == "y":
        play_game()
        play_more = input("Do you want to play again? Type 'y' or 'n':\n ")

# Start the game
if __name__ == "__main__":
    main()
