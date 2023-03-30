from ten_thousand.game_logic import GameLogic

dice_roller = GameLogic.roll_dice


def play(roller):
    global dice_roller
    dice_roller = roller
    global game
    game = GameLogic()
    intro()


def intro():
    print('Welcome to Ten Thousand')
    print('(y)es to play or (n)o to decline')
    choice = input('> ')
    options.get(choice.strip(), lambda: print('invalid input'))()


def decline():
    print('OK. Maybe another time')


def start_round():
    game.new_round()
    print(f'Starting round {game.round}')
    roll_dice()


def roll_dice():
    print(f'Rolling {game.dice_left} dice...')
    dice = dice_roller(game.dice_left)
    dice_string = '*** '
    for x in dice:
        dice_string = dice_string + str(x) + ' '
    dice_string += '***'
    print(dice_string)
    if GameLogic.calculate_score(dice) == 0:
        print('****************************************')
        print('**        Zilch!!! Round over         **')
        print('****************************************')
        print(f'You banked 0 points in round {game.round}')
        print(f'Total score is {game.total_points} points')
        start_round()
        return
    format_choice = False
    choice = ' '
    while not format_choice and choice != 'q':
        print('Enter dice to keep, or (q)uit:')
        choice = input('> ')
        if choice == 'q':
            quit_game()
            format_choice = True
        else:
            format_choice = check_cheating(dice, choice)
            if not format_choice:
                print(dice_string)
    if choice != 'q':
        score = GameLogic.calculate_score(game.set_aside(format_choice.strip(), dice))
        game.set_current_points(score)
        if len(game.set_aside_dice) == 6:
            game.hot_dice()
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


def check_cheating(dice, choice):
    dice_numbers = ['1', '2', '3', '4', '5', '6']
    other_numbers = ['0', '7', '8', '9']
    number_string = ''
    dice_list = list(dice)
    for x in choice:
        if x in dice_numbers:
            if int(x) not in dice_list:
                print(f'Cheater!!! Or possibly made a typo...')
                return False
            else:
                dice_list.remove(int(x))
                number_string += f'{x} '
        elif x in other_numbers:
            print(f'{x} is not a valid number')
            return False
    return number_string


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
