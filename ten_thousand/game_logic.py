import random

class GameLogic:
    @staticmethod
    def calculate_score(dice_roll):
        dice_counts = [dice_roll.count(i) for i in range(1, 7)]
        score = 0

        for i, count in enumerate(dice_counts):
            if count >= 3:
                if i == 0:
                    score += (1000 * (2 ** (count - 3)))
                elif i == 4:
                    score += (500 * (2 ** (count - 3)))
            elif count > 0:
                if i == 0:
                    score += (count * 100)
                elif i == 4:
                    score += (count * 50)


        # for i, count in enumerate(dice_counts):
        #     if count >= 3:
        #         if i == 0:
        #             score += (2**(count-3) * 1000)
        #         elif i == 4:
        #             score += (2**(count-3) * 500)
        #         else:
        #             score += (count * 100 * (i + 1))
        #     elif count > 0:
        #         if i == 0:
        #             score += (count * 100)
        #         elif i == 4:
        #             score += (count * 50)

        #
        # for count in dice_counts:
        #     if count >= 3:
        #         if count == 3:
        #             score += (count * 100) if count == 3 else (count * 100 * 2)
        #         else:
        #             score += (count * 100 * 2)
        #     elif count > 0:
        #         score += (count * 100)

        return score

    @staticmethod
    def roll_dice(num_dice):
        return tuple(random.randint(1, 6) for _ in range(num_dice))
