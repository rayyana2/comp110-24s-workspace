"""demonstrates while loops by finding low value in string"""

cards: str = "5235"
low: int = cards[0]

card_idx: int = 0

#look at each value in a string
while card_idx < len(cards):
    current_card = int(cards[card_idx])
    if current_card < int(low):
        low = cards[card_idx]
    else:
        card_idx = card_idx + 1

print(low)