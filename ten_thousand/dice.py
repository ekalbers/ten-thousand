from game_logic import GameLogic
from textwrap import dedent

intro = dedent(
    '''
    Welcome to Ten Thousand
    (y) to play or (n)o to decline
    '''
)


def dice(game):
    print(intro)
    x = input('> ')
    play = False
    if x.lower() == 'y':
        play = True
    while play:
        print(f'Starting round {game.round}')
        if game.dice_left > 1:
            print(f'Rolling {game.dice_left} dice...')
        else:
            print(f'Rolling {game.dice_left} die...')
        dice = GameLogic.roll_dice(game.dice_left)
        dice_str = '*** '
        for x in dice:
            dice_str = dice_str + str(x) + ' '
        dice_str += '***'
        print(dice_str)
        print('Enter dice to keep, or (q)uit:')
        x = input('> ')
        if x == 'q':
            play = False
            print(f'Thanks for playing. You earned {game.total_points}')
            break
        points = GameLogic.calculate_score(game.set_aside(x, dice))
        game.set_current_points(points)
        print(f'You have {game.current_points} unbanked points and {game.dice_left} dice remaining')
        print('(r)oll again, (b)ank your points or (q)uit:')
        x = input('> ')
        if x == 'q':
            play = False
            print(f'Thanks for playing. You earned {game.total_points}')
            break
        elif x == 'b':
            game.bank_points(game.current_points)
            print(f'You banked {game.current_points} points in round {game.round}')
        game.new_round()


if __name__ == '__main__':
    game = GameLogic()
    dice(game)
