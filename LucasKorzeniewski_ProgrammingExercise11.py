import random

# Rank and suit labels used to translate card numbers into readable text
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']


class Deck():
    def __init__(self, size):
        # Build the full list of card numbers 0 through size - 1
        self.card_list = [i for i in range(size)]
        self.cards_in_play_list = []
        self.discards_list = []

        # Shuffle right away so the deck order is randomized before play
        random.shuffle(self.card_list)

    def deal(self):
        # Reshuffle discards back into the deck if we run out of cards
        if len(self.card_list) < 1:
            random.shuffle(self.discards_list)
            self.card_list = self.discards_list
            self.discards_list = []
            print('Reshuffling...!!!')

        # Take the top card off the deck and mark it as in play
        new_card = self.card_list.pop()
        self.cards_in_play_list.append(new_card)
        return new_card

    def new_hand(self):
        # Move every card currently in play into the discard pile
        self.discards_list += self.cards_in_play_list
        self.cards_in_play_list.clear()


def card_to_string(card_number):
    # Use integer division to find which suit block the card falls in
    suit = SUITS[card_number // 13]

    # Use the remainder to find the rank within that suit
    rank = RANKS[card_number % 13]

    return f'{rank} of {suit}'


def deal_hand(deck, num_cards):
    # Draw num_cards fresh cards from the deck to build the starting hand
    hand = []
    for i in range(num_cards):
        hand.append(deck.deal())

    return hand


def display_hand(hand):
    # Show a 1-based position next to each card so choices are intuitive
    for index, card in enumerate(hand):
        print(f'{index + 1}: {card_to_string(card)}')


def get_replacement_choices(hand_size):
    # Ask which positions to swap out during the draw phase
    prompt = ('Enter the numbers of the cards you want to replace '
              '(e.g. 1, 3, 5), or press Enter to keep your whole hand: ')
    user_input = input(prompt)

    # An empty response means the player keeps every card as is
    if user_input.strip() == '':
        return []

    # Convert the comma separated numbers into zero-based list indexes
    choices = [int(value.strip()) - 1 for value in user_input.split(',')]

    return choices


def draw_new_cards(deck, hand, choices):
    # Only replace the positions the player actually selected
    for position in choices:
        hand[position] = deck.deal()

    return hand


def play_poker_round():
    # Build a standard 52 card deck for this round
    deck = Deck(52)

    # Deal the initial five card poker hand
    hand = deal_hand(deck, 5)

    print('Your hand:')
    display_hand(hand)

    # Find out which cards the player wants to trade in
    choices = get_replacement_choices(len(hand))

    # Replace the chosen cards with new ones from the deck
    hand = draw_new_cards(deck, hand, choices)

    print('\nYour final hand:')
    display_hand(hand)

    # Send this round's cards to the discard pile before the next round
    deck.new_hand()


def main():
    # Kick off a single round of five card draw poker
    play_poker_round()


if __name__ == '__main__':
    main()