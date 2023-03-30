import random


class GameLogic:
    def __init__(self):
        self.total_points = 0
        self.current_points = 0
        self.round = 0
        self.set_aside_dice = []
        self.dice_left = 6

    @staticmethod
    def calculate_score(dice_roll):
        dice_counts = [dice_roll.count(i) for i in range(1, 7)]
        score = 0
        three_of_a_kind_count = 0

        if sorted(dice_counts) == [0, 0, 0, 2, 2, 2]:
            score = 1500
        elif dice_counts == [1, 1, 1, 1, 1, 1]:
            score = 1500
        else:
            for i, count in enumerate(dice_counts):
                if count >= 3:
                    if i == 0:
                        score += (1000 * (1 + (count - 3)))
                    elif i == 4:
                        score += (500 * (1 + (count - 3)))
                    else:
                        score += ((i + 1) * 100 * (1 + (count - 3)))
                    three_of_a_kind_count += 1
                elif count > 0:
                    if i == 0:
                        score += (count * 100)
                    elif i == 4:
                        score += (count * 50)

        return score

    @staticmethod
    def validate_keepers(roll, keep):
        test_roll = list(roll)
        for x in keep:
            if x in test_roll:
                test_roll.remove(x)
            else:
                return False
        return True

    @staticmethod
    def get_scorers(dice):
        scorers = []
        numbers = [0, 0, 0, 0]
        for x in dice:
            if x in [1, 5]:
                scorers.append(x)
            else:
                numbers[x - 2] += 1
        for i, count in enumerate(numbers):
            if count > 2:
                scorers.extend([i + 2] * (count - 2))
        return scorers

    def new_round(self):
        self.current_points = 0
        self.increment_round()
        self.set_aside_dice = []
        self.dice_left = 6

    def hot_dice(self):
        self.dice_left = 6
        self.set_aside_dice = []

    def set_current_points(self, points):
        self.current_points = self.current_points + points

    def set_aside(self, string, dice):
        chosen_dice = string.split(' ')
        send_back = ()
        for x in chosen_dice:
            if int(x) in dice:
                send_back = send_back + (int(x),)
                self.set_aside_dice += [int(x)]
                self.dice_left -= 1
        return send_back

    def bank_points(self):
        self.total_points += self.current_points

    def increment_round(self):
        self.round += 1

    @staticmethod
    def roll_dice(dice):
        return tuple(random.randint(1, 6) for _ in range(dice))
