order = '23456789TJQKA'

def player_wins_high_card(hand1, hand2):
    faces1 = [card[0] for card in hand1]
    faces2 = [card[0] for card in hand2]
    high_face1 = max([order.index(face) for face in faces1])
    high_face2 = max([order.index(face) for face in faces2])
    if high_face1 > high_face2:
        return True
    if high_face2 > high_face1:
        return False
    # suit determines winner 
    suit_order = "SCDH"
    high_suit1 = hand1[faces1.index(high_face1)][1]
    high_suit2 = hand1[faces1.index(high_face1)][1]
    return high_suit1 > high_suit2

def player_wins_dispute(hand1, hand2, size):
    faces1 = [card[0] for card in hand1]
    faces2 = [card[0] for card in hand2]
    pair1 = 0
    for card in faces1:
        if faces1.count(card) == size:
            if order.index(card) > pair1:
                pair1 = order.index(card)
    pair2 = 0
    for i in faces2:
        if faces2.count(i) == size:
            if order.index(i) > pair2:
                pair2 = order.index(i)

    return  pair1 > pair2

def is_straight(faces):
    for face in faces:
        idex = order.index(face)
        try:
            if all([order[idex + i] in faces for i in range(1, 5)]):
                return True
        except IndexError:
            pass
    return False

def is_flush(suits):
    return all([suit == suits[0] for suit in suits])

def rank_hand(hand):
    suits = [card[1] for card in hand]
    faces = [card[0] for card in hand]
    flush = is_flush(suits)
    straight = is_straight(faces)
    if flush and all([face in faces for face in 'TJQKA']):
        return 9 # Royal flush 
    if flush and straight:
        return 8 # straight flush
    if any([faces.count(face) == 4 for face in order]):
        return 7 # 4 of a kind
    if any([faces.count(face) == 3 for face in order]) and any([faces.count(face) == 2 for face in order]):
        return 6 # Full house
    if flush:
        return 5 # flush
    if straight:
        return 4 # straight
    if any([faces.count(face) == 3 for face in order]):
        return 3 # three of a kind
    if sum([faces.count(face) == 2 for face in order]) == 2:
        return 2 # two pairs
    if any([faces.count(face) == 2 for face in order]):
        return 1 # one pair
    return 0


with open("resources\poker.txt") as file:
    all_hands = file.readlines()
    score = 0
    for hand in all_hands:
        cards = hand.split()
        player1 = cards[0:5]
        player2 = cards[5::]
        rank1 = rank_hand(player1)
        rank2 = rank_hand(player2)
        if rank1 > rank2:
            score += 1
        if rank1 == rank2:
            if rank1 == 0 and player_wins_high_card(player1, player2):
                score += 1
            elif (rank1 == 1 or rank1 == 2) and player_wins_dispute(player1, player2, 2):
                print("player won pair dispute", player1, player2)
                score += 1

            elif (rank1 == 3 or rank1 == 6) and player_wins_dispute(player1, player2, 3):
                score += 1

            elif rank1 == 7 and player_wins_dispute(player1, player2, 4):
                score += 1

            elif (rank1 == 4 or rank1 == 8) and player_wins_high_card(hand1, hand2):
                score += 1

print(score)