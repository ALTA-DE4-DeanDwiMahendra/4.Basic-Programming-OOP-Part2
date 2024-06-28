def playing_domino(cards, deck):
    best_card = []
    max_sum = -1
    
    for card in cards:
        if deck[0] in card or deck[1] in card:
            card_sum = sum(card)
            if card_sum > max_sum:
                max_sum = card_sum
                best_card = card
    
    return best_card

if __name__ == "__main__":
    print(playing_domino([[6, 5], [3, 4], [2, 1], [3, 3]], [4, 3]))  # [3, 4]
    print(playing_domino([[6, 5], [3, 3], [3, 4], [2, 1]], [3, 6]))  # [6, 5]
    print(playing_domino([[6, 6], [2, 4], [3, 6]], [5, 1]))         # []
