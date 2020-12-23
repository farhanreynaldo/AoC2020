from collections import deque

SAMPLE = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10"""

def parse_decks(raw):
    player1, player2 = raw.split("\n\n")
    player1_deck = deque([int(card) for card in player1.split("\n")[1:]])
    player2_deck = deque([int(card) for card in player2.split("\n")[1:]])
    return player1_deck, player2_deck


def play(p1_deck, p2_deck):
    while p1_deck and p2_deck:
        p1_card = p1_deck.popleft()
        p2_card = p2_deck.popleft()
        if p1_card > p2_card:
            p1_deck.extend([p1_card, p2_card])
        else:
            p2_deck.extend([p2_card, p1_card])

    winner = p1_deck or p2_deck
    return sum(
        card * score for card, score in zip(reversed(winner), range(1, len(winner) + 1))
    )

assert play(*parse_decks(SAMPLE)) == 306
day22 = open('input/day22.txt').read().strip()
print(play(*parse_decks(day22)))

def winning_score(deck):
    return sum(
        card * score for card, score in zip(reversed(deck), range(1, len(deck) + 1))
    )

def play_recursive(p1_deck, p2_deck):
    seen = set()
    while p1_deck and p2_deck:
        current_decks = (tuple(p1_deck), tuple(p2_deck))
        if current_decks in seen:
            return (p1_deck, 'p1')
        else:
            seen.add(current_decks)

        p1_card = p1_deck.popleft()
        p2_card = p2_deck.popleft()
        winner = None
        if p1_card <= len(p1_deck) and p2_card <= len(p2_deck):
            p1_subdeck = deque(list(p1_deck)[:p1_card])
            p2_subdeck = deque(list(p2_deck)[:p2_card])
            winner = play_recursive(p1_subdeck, p2_subdeck)[1]
        
        if winner == 'p1':
            p1_deck.extend([p1_card, p2_card])
        elif winner == 'p2':
            p2_deck.extend([p2_card, p1_card])
        elif p1_card > p2_card:
            p1_deck.extend([p1_card, p2_card])
        else:
            p2_deck.extend([p2_card, p1_card])

    return (p1_deck, 'p1') if p1_deck else (p2_deck, 'p2')

assert winning_score(play_recursive(*parse_decks(SAMPLE))[0]) == 291
print(winning_score(play_recursive(*parse_decks(day22))[0]))