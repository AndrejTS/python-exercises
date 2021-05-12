STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.word = word
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.letters = set()

    def guess(self, char):
        if self.status != STATUS_ONGOING:
            raise ValueError('Game is over!')
        if char not in self.word or char in self.letters:
            self.remaining_guesses -= 1
            if self.remaining_guesses < 0:
                self.status = STATUS_LOSE
        self.letters.add(char)
        if set(self.word) & self.letters == set(self.word):
            self.status = STATUS_WIN

    def get_masked_word(self):
        f = lambda l: l if l in self.letters else '_'
        return ''.join(map(f, self.word))

    def get_status(self):
        return self.status