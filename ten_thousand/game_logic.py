import random


class GameLogic:
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
    def roll_dice(num_dice):
        return tuple(random.randint(1, 6) for _ in range(num_dice))
