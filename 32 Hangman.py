"""
In this exercise, we will finish building Hangman. In the game of Hangman, the
player only has 6 incorrect guesses (head, body, 2 legs, and 2 arms) before
they lose the game.

In Part 1, we loaded a random word list and picked a word from it. In Part 2,
we wrote the logic for guessing the letter and displaying that information to
the user. In this exercise, we have to put it all together and add logic for
handling guesses.

Copy your code from Parts 1 and 2 into a new file as a starting point. Now add
the following features:

Only let the user guess 6 times, and tell the user how many guesses they have
left. Keep track of the letters the user guessed. If the user guesses a letter
they already guessed, don’t penalize them - let them guess again.
"""

from random import randrange


class Hangman:
    def __init__(self):
        self.guesses = 6
        self.history = []
        self.answer = self._get_word()
        self.state = ['_'] * len(self.answer)
        print('Welcome to Hangman! ({})'.format(self.answer))
        self.display()
        while not self.done():
            self.guess()

    def display(self):
        print(' '.join(self.state))

    def guess(self):
        g = input('Guess your letter:')
        if g in self.history:
            print('You\'ve already guessed that')
        else:
            self.history.append(g)
            if g in self.answer:
                for i, v in enumerate(self.answer):
                    if v == g:
                        self.state[i] = g
                self.display()
            else:
                self.guesses -= 1
                print('Incorrect! {} Guesses remaining.'.format(self.guesses))
            return g

    def done(self):
        if self.guesses == 0:
            print('You Lose!')
            return True
        elif '_' not in self.state:
            print('You Win!')
            return True
        else:
            return False

    @staticmethod
    def _get_word():
        with open('assets/sowpods.txt', 'rt') as f:
            words = [x.strip() for x in f.readlines()]
            return words[randrange(len(words))]


h = Hangman()
