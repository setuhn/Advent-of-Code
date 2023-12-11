import re

def increment_cards_inventory(cards_inventory, card_idx, add):
    if card_idx not in cards_inventory.keys():
        cards_inventory[card_idx] = 0

    cards_inventory[card_idx] += add

if __name__ == '__main__':

    with open(f'day_4.txt') as data:

        regex_numbers: re.Pattern = re.compile(r'(\d+)')
        points = 0

        cards_inventory = {}

        for card in data.readlines():
            card_idx, numbers = card.strip().split(':')
            card_idx = int(regex_numbers.search(card_idx).group())

            increment_cards_inventory(cards_inventory, card_idx, 1)

            numbers_win, numbers_our = [set(regex_numbers.findall(n)) for n in numbers.split('|')]
            intersection = numbers_win.intersection(numbers_our)

            if intersection:
                points += 2**(len(intersection)-1)

                for n in range(1, len(intersection)+1):
                    increment_cards_inventory(cards_inventory, card_idx + n, cards_inventory[card_idx])

    print(f'Answer to part 1: {points}')
    print(f'Answer to part 2: {sum(cards_inventory.values())}')