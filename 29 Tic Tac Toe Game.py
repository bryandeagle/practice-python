"""
The next step is to put all these three components together to make a
two-player Tic Tac Toe game! Your challenge in this exercise is to use
the functions from those previous exercises all together in the same
program to make a two-player game that you can play with a friend. There
are a lot of choices you will have to make when completing this exercise,
so you can go as far or as little as you want with it.

You should keep track of who won - if there is a winner, show a
congratulatory message on the screen. If there are no more moves left,
don’t ask for the next player’s move!
"""

import colorama


class TicTacToe:
    def __init__(self):
        colorama.init()
        self.moves = {'TL': (0, 0), 'TC': (0, 1), 'TR': (0, 2),
                      'ML': (1, 0), 'MC': (1, 1), 'MR': (1, 2),
                      'BL': (2, 0), 'BC': (2, 1), 'BR': (2, 2)}
        self.state = [[' ', ' ', ' '],
                      [' ', ' ', ' '],
                      [' ', ' ', ' ']]
        self.player = 'X'

    def __del__(self):
        colorama.deinit()

    def __repr__(self):
        b, r = colorama.Fore.BLUE, colorama.Style.RESET_ALL
        return f' {self.state[0][0]} {b}┃{r} ' \
               f'{self.state[0][1]} {b}┃{r} {self.state[0][2]} \n' \
               f'{b}━━━╋━━━╋━━━{r}\n {self.state[1][0]} {b}┃{r} ' \
               f'{self.state[1][1]} {b}┃{r} {self.state[1][2]} \n' \
               f'{b}━━━╋━━━╋━━━{r}\n {self.state[2][0]} {b}┃{r} ' \
               f'{self.state[2][1]} {b}┃{r} {self.state[2][2]} '

    def move(self, move):
        if move == 'Q':
            quit()
        real = self.moves[move]
        if self.state[real[0]][real[1]] != ' ':
            print('Invalid Move')
        else:
            self.state[real[0]][real[1]] = self.player
            self.player = {'X': 'O', 'O': 'X'}[self.player]

    def evaluate(self):
        if ['X', 'X', 'X'] in [self.state[0][:], self.state[1][:],
                               self.state[2][:], self.state[:][0],
                               self.state[:][1], self.state[:][2]]:
            print('X Wins!')
            return 'X'
        elif (self.state[1][1] == 'X') and ['X', 'X'] in \
                [[self.state[0][0], self.state[2][2]],
                 [self.state[0][2], self.state[2][0]]]:
            print('X Wins!')
            return 'X'
        elif ['O', 'O', 'O'] in [self.state[0][:], self.state[1][:],
                                 self.state[2][:], self.state[:][0],
                                 self.state[:][1], self.state[:][2]]:
            print('O Wins!')
            return 'O'
        elif (self.state[1][1] == 'O') and ['O', 'O'] in \
                [[self.state[0][0], self.state[2][2]],
                 [self.state[0][2], self.state[2][0]]]:
            print('O Wins!')
            return 'O'


game = TicTacToe()
while not game.evaluate():
    move = input('Player {} Move:'
                 .format(game.player))
    game.move(move)
    print(game)
