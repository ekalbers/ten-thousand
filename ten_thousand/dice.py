from game_logic import GameLogic


def intro():
    global options
    print('welcome to Ten Thousand')
    print('(y)es to play or (n)o to decline')
    choice = input('> ')
    options.get(choice, lambda: print('invalid input'))()


def decline():
    print('OK. Maybe another time')


def start_round():
    game.new_round()
    print(f'Starting round {game.round}')
    roll_dice()


def roll_dice():
    print(f'Rolling {game.dice_left} dice...')
    dice = game.roll_dice()
    dice_string = '*** '
    for x in dice:
        dice_string = dice_string + str(x) + ' '
    dice_string += '***'
    print(dice_string)
    print('Enter dice to keep, or (q)uit:')
    choice = input('> ')
    if choice == 'q':
        quit_game()
    else:
        score = GameLogic.calculate_score(game.set_aside(choice, dice))
        game.set_current_points(score)
        print(f'You have {game.current_points} unbanked points and {game.dice_left} dice remaining')
        print('(r)oll again, (b)ank your points or (q)uit:')
        choice = input('> ')
        options.get(choice, lambda: print('invalid input'))()


def bank():
    print(f'You banked {game.current_points} points in round {game.round}')
    game.bank_points()
    print(f'Total score is {game.total_points} points')
    start_round()


def quit_game():
    print(f'Thanks for playing. You earned {game.total_points} points')


options = {
    'y': start_round,
    'b': bank,
    'r': roll_dice,
    'q': quit_game,
    'n': decline
}


if __name__ == '__main__':
    game = GameLogic()
    intro()
