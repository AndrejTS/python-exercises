class BowlingGame:
    def __init__(self):
        self.throws = []
        self.num_frames = 0
        self.bonus_rolls = 0
        self.balls = 0 # number throwed balls in one frame 


    def roll(self, pins):
        if pins > 10 or pins < 0:
            raise Exception('Must be 0-10')
        if self.bonus_rolls:
            if self.throws[-1] != 10 and sum(self.throws[-2:]) != 10:
                if pins == 10:
                    raise Exception('the_second_bonus_rolls_after_a_strike_in_the_last_frame_cannot_be_a_strike_if_the_first_one_is_not_a_strike')
                elif pins + self.throws[-1] > 10:
                    raise Exception('two_bonus_rolls_after_a_strike_in_the_last_frame_cannot_score_more_than_10_points')
            self.throws.append(pins)
            self.bonus_rolls -= 1
            return
        if self.num_frames == 10 and self.bonus_rolls == False:
            raise Exception('cannot_roll_if_game_already_has_ten_frames')
        elif pins == 10:
            self.throws.append(10)
            self.num_frames += 1
        elif pins < 10:
            if self.throws:
                if self.throws[-1] != 10 and sum(self.throws[-2:]) != 10:
                    if pins + self.throws[-1] > 10:
                        raise Exception('two_rolls_in_a_frame_cannot_score_more_than_10_points')
            self.balls += 1
            if self.balls == 2:
                self.num_frames += 1
                self.balls = 0
            self.throws.append(pins)
        if self.num_frames == 10:
            if self.throws[-1] == 10:
                self.bonus_rolls = 2
            elif sum(self.throws[-2:]) == 10:
                self.bonus_rolls = 1
            

    def score(self):
        _score = 0
        frames_calculated = 0
        i = 0
        while i != len(self.throws):
            if self.throws[i] == 10: # strike
                _score += 10 + self.throws[i+1] + self.throws[i+2]
                i += 1
            elif self.throws[i] + self.throws[i+1] == 10: # spare
                _score += 10 + self.throws[i+2]
                i += 2
            else:
                _score += self.throws[i] + self.throws[i+1] # open frame
                i += 2
            frames_calculated += 1
            if frames_calculated == 10:
                break
        return _score
