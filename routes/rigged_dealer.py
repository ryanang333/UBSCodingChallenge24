from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Define card values and strengths
RANKS = {str(i): i for i in range(2, 11)}
RANKS.update({"J": 11, "Q": 12, "K": 13, "A": 14})
SUITS = {'C': 1, 'D': 2, 'H': 3, 'S': 4}

# Card evaluation functions
def evaluate_hand(hand):
    # Count the ranks and suits
    rank_count = {rank: 0 for rank in RANKS}
    suit_count = {suit: 0 for suit in SUITS}
    
    for card in hand:
        rank, suit = card[:-1], card[-1]
        rank_count[rank] += 1
        suit_count[suit] += 1
    
    # Identify hand strength
    # Simplified for the sake of example; you can expand this with full rules
    counts = sorted(rank_count.values(), reverse=True)
    if counts == [4, 1]:
        return "Four of a kind"
    elif counts == [3, 2]:
        return "Full house"
    elif counts == [3, 1, 1]:
        return "Three of a kind"
    elif counts == [2, 2, 1]:
        return "Two pair"
    elif counts == [2, 1, 1, 1]:
        return "One pair"
    else:
        return "High card"

def riffle_shuffle(deck):
    # Assume this is your implementation of riffle shuffle
    if len(deck) <= 1:
        return deck  # No shuffling needed
    mid = len(deck) // 2
    left = deck[:mid]
    right = deck[mid:]
    shuffled = []
    for l, r in zip(left, right):
        shuffled.append(l)
        shuffled.append(r)
    shuffled.extend(left[len(right):])  # Add any remaining cards
    shuffled.extend(right[len(left):])  # In case left is larger
    return shuffled

def cut_deck(deck, cut_index):
    return deck[cut_index:] + deck[:cut_index]

def rig_game(round_info):
    actions = []
    number_of_players = round_info['numberOfPlayers']
    hand_size = round_info['handSize']
    winning_player = round_info['winningPlayer']
    starting_deck = round_info['startingDeck']

    # Create a copy of the starting deck for shuffling and dealing
    shuffled_deck = starting_deck.copy()
    
    print(f"Initial deck size: {len(shuffled_deck)}")

    # Perform a shuffle
    shuffled_deck = riffle_shuffle(shuffled_deck)
    print(f"Deck size after shuffling: {len(shuffled_deck)}")

    # Perform a cut at a fixed index, ensure it's valid
    cut_index = 10  # Example cut index, adjust as needed
    if 0 < cut_index < len(shuffled_deck):
        shuffled_deck = cut_deck(shuffled_deck, cut_index)
    else:
        raise ValueError(f"Invalid cut index: {cut_index}")
    
    print(f"Deck size after cutting: {len(shuffled_deck)}")

    # Check deck length after shuffling and cutting
    if len(shuffled_deck) < number_of_players * hand_size:
        raise ValueError("Deck size is not sufficient after shuffling and cutting.")

    # Deal cards
    hands = deal_cards(shuffled_deck, number_of_players, hand_size)

    # Evaluate hands and determine actions for rigging
    for i, hand in enumerate(hands):
        strength = evaluate_hand(hand)
        print(f"Player {i} hand: {hand} -> {strength}")

    return actions

def deal_cards(deck, number_of_players, hand_size):
    # Check if we have enough cards to deal
    if len(deck) < number_of_players * hand_size:
        raise ValueError("Not enough cards in the deck to deal.")

    hands = [[] for _ in range(number_of_players)]
    for i in range(hand_size):
        for j in range(number_of_players):
            # Pop the top card from the deck for each player in round-robin fashion
            hands[j].append(deck.pop(0))
    return hands

# def rig_game(round_info):
#     actions = []
#     number_of_players = round_info['numberOfPlayers']
#     hand_size = round_info['handSize']
#     winning_player = round_info['winningPlayer']
#     starting_deck = round_info['startingDeck']

#     # Create a copy of the starting deck for shuffling and dealing
#     shuffled_deck = starting_deck.copy()

#     # Perform a shuffle and a cut
#     shuffled_deck = riffle_shuffle(shuffled_deck)
#     shuffled_deck = cut_deck(shuffled_deck, 10)  # Cut at index 10, example

#     # Check deck length after shuffling
#     if len(shuffled_deck) < number_of_players * hand_size:
#         raise ValueError("Deck size is not sufficient after shuffling.")

#     # Deal cards
#     hands = deal_cards(shuffled_deck, number_of_players, hand_size)

#     # Evaluate hands and determine actions for rigging
#     for i, hand in enumerate(hands):
#         strength = evaluate_hand(hand)
#         print(f"Player {i} hand: {hand} -> {strength}")

#     return actions


@app.route('/riggedDealer', methods=['POST'])
def rigged_dealer():
    data = request.get_json()
    rounds = data.get('rounds', [])
    
    responses = []
    for round_info in rounds:
        actions = rig_game(round_info)
        responses.append({"actions": actions})
    
    return jsonify(responses)

if __name__ == '__main__':
    app.run(debug=True)