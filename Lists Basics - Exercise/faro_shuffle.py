cards = input().split()
number_shuffles = int(input())

for shuffle in range(number_shuffles):
    final_deck = []
    middle_deck = len(cards) // 2
    left_side = cards[0:middle_deck]
    right_side = cards[middle_deck:]
    for card in range(len(left_side)):
        final_deck.append(left_side[card])
        final_deck.append(right_side[card])
    cards = final_deck

print(cards)