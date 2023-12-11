from collections import Counter

def find_type_1(hand):
    counts = Counter(hand)

    val = list(counts.values())
    max_val = max(val)

    if max_val == 5:
        return 7
    
    if max_val == 4:
        return 6
    
    if max_val == 3 and 2 in val:
        return 5
    
    if max_val == 3:
        return 4
    
    if max_val == 2 and val.count(2) == 2:
        return 3
    
    if max_val == 2:
        return 2
    
    else:
        return 1
    
def find_type_2(hand):
    counts = Counter(hand)

    val = list(counts.values())
    j_num = counts[0]
    max_val = max(val)

    # If all the cards are the same or there are no J go directly to return
    if max_val == 5 or j_num ==0:
        pass

    # If J is the most numerous card find the second numerous card and transform 0 into that card's value
    elif j_num == max_val and val.count(max_val) == 1:
        card_max_value = counts.most_common(2)[1][0]
        hand = [card_max_value if card == 0 else card for card in hand]

    # Otherwise, find the most numerous card with the highest value and transfor 0 into that card's value
    else:
        card_max_value = max([card for card in hand if counts[card] == max_val])
        hand = [card_max_value if card == 0 else card for card in hand]
    
    return find_type_1(hand)

def part_1(data):
    game = {}
    correspondance = {
        'A': 14,
        'K': 13,
        'Q': 12,
        'J': 11,
        'T': 10
    }

    for line in data:
        hand, bid = line.strip().split(' ')
        
        # Change the hands in a list of int
        hand = [int(card) if card.isdigit() else correspondance[card] for card in hand]
        bid = int(bid)

        # Get the type of hands and add it as the first value of the hand
        hand.insert(0, find_type_1(hand)) 
        # list the hands
        game[tuple(hand)] = bid

    # Sort the list
    game_hands = list(game.keys())
    game_hands.sort()

    return sum([game[hand] * (idx+1) for idx, hand in enumerate(game_hands)])

def part_2(data):
    game = {}
    correspondance = {
        'A': 14,
        'K': 13,
        'Q': 12,
        'J': 0,
        'T': 10
    }

    for line in data:
        hand, bid = line.strip().split(' ')
        
        # Change the hands in a list of int
        hand = [int(card) if card.isdigit() else correspondance[card] for card in hand]
        bid = int(bid)

        # Get the type of hands and add it as the first value of the hand
        hand.insert(0, find_type_2(hand))
        
        # list the hands
        game[tuple(hand)] = bid

    # Sort the list
    game_hands = list(game.keys())
    game_hands.sort()

    return sum([game[hand] * (idx+1) for idx, hand in enumerate(game_hands)])

if __name__ == '__main__':

    with open(f'day_7.txt') as data:
        lines = data.readlines()
        print(f'Answer to part 1: {part_1(lines)}')
        print(f'Answer to part 2: {part_2(lines)}')
