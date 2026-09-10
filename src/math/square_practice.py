import random

from utils.console import console

class SquareTester:
    def __init__(self):
        self.roots = range(1, 26)
        self.results = None
        # self.squares = [x**2 for x in self.roots]

    def test_squares_loop(self):
        correct = 0
        seen = {}
        while len(self.roots) > 0:
            if len(self.roots) == 1:
                 r = self.roots[0]
            else:
                r_pos = random.randint(0, len(self.roots) - 1)
                r = self.roots[r_pos]
            console.print(f'Square {r}')
            response = int(input(''))
            self.roots = [x for x in self.roots if x != r]
            if response == r ** 2:
                console.print('Correct!')
                correct += 1
            else:
                console.print('Incorrect!')

        self.results = (correct/25) * 100

    def display_results(self):
        if self.results:
            console.print(f'Your last test session results: {self.results:.2f}%')
        else:
            console.print('You have no results')

    def intro(self):
        self.display_results()
        console.print('Do you want to review?')
        choice = int(input(''))
        if choice == 1:
            self.test_squares_loop()
            self.intro()
        elif choice == 0:
            console.print('Good bye.')
        else:
            console.print('Invalid Choice', style='red bold')
            self.intro()

if __name__=='__main__':
    tester = SquareTester()
    tester.intro()
