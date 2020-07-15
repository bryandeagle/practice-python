"""
Let’s continue building Hangman. In the game of Hangman, a clue word is given
by the program that the player has to guess, letter by letter. The player
guesses one letter at a time until the entire word has been guessed. (In the
actual game, the player can only guess 6 letters incorrectly before losing).

Let’s say the word the player has to guess is “EVAPORATE”. For this exercise,
write the logic that asks a player to guess a letter and displays letters in
the clue word that were guessed correctly. For now, let the player guess an
infinite number of times until they get the entire word. As a bonus, keep
track of the letters the player guessed and display a different message if the
player tries to guess that letter again. Remember to stop the game when all
the letters have been guessed correctly! Don’t worry about choosing a word
randomly or keeping track of the number of guesses the player has remaining -
we will deal with those in a future exercise.

An example interaction can look like this:

>>> Welcome to Hangman!
_ _ _ _ _ _ _ _ _
>>> Guess your letter: S
Incorrect!
>>> Guess your letter: E
E _ _ _ _ _ _ _ E
"""

from random import randrange


class Hangman:
    def __init__(self):
        self.answer = self._get_word()
        self.state = ['_'] * len(self.answer)
        print('Welcome to Hangman! ({})'.format(self.answer))
        self.display()
        while not self.won():
            self.guess()

    def display(self):
        print(' '.join(self.state))

    def guess(self):
        g = input('Guess your letter:')
        if g in self.answer:
            for i, v in enumerate(self.answer):
                if v == g:
                    self.state[i] = g
            self.display()
        else:
            print('Incorrect!')
        return g

    def won(self):
        return '_' not in self.state

    @staticmethod
    def _get_word():
        with open('assets/sowpods.txt', 'rt') as f:
            words = [x.strip() for x in f.readlines()]
            return words[randrange(len(words))]


h = Hangman()
