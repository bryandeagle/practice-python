"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays
(using input), compare them, print out a message of congratulations to
the winner, and ask if the players want to start a new game)

Remember the rules:
- Rock beats scissors
- Scissors beats paper
- Paper beats rock
"""

acceptable = ['rock', 'paper', 'scissors']

#    P1: R  P  S    # P2
game = [[0, 1, 2],  # R
        [2, 0, 1],  # P
        [1, 2, 0]]  # S

player_1 = input('Player 1 choice:').lower()
while player_1 not in acceptable:
    player_1 = input('Not Accepted. Choose again:').lower()
p1 = acceptable.index(player_1)

player_2 = input('Player 2 choice:').lower()
while player_2 not in acceptable:
    player_2 = input('Not Accepted. Choose again:').lower()
p2 = acceptable.index(player_2)

result = game[p2][p1]
if result == 0:
    print('Tie!')
else:
    print('Player {} Wins!'.format(result))
