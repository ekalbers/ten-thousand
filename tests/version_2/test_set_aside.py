import pytest
from ten_thousand.game_logic import GameLogic


# @pytest.mark.skip('todo')
@pytest.mark.version_2
def test_set_aside():
    game = GameLogic()
    x = game.set_aside('1 5', [1, 2, 3, 4, 5, 6])
    set_aside_dice = game.set_aside_dice
    expected1 = (1, 5)
    expected2 = [1, 5]
    assert x == expected1
    assert set_aside_dice == expected2


@pytest.mark.version_2
def test_total_points():
    total = GameLogic()
    expected = 0
    assert total.total_points == expected


@pytest.mark.version_2
def test_bank_points():
    game = GameLogic()
    game.set_current_points(100)
    game.bank_points()
    total = game.total_points
    expected = 100
    assert total == expected


@pytest.mark.version_2
def test_bank_points_zero():
    game = GameLogic()
    game.set_current_points(0)
    game.bank_points()
    total = game.total_points
    expected = 0
    assert total == expected


@pytest.mark.version_2
def test_bank_points_negative():
    game = GameLogic()
    game.set_current_points(-100)
    game.bank_points()
    total = game.total_points
    expected = -100
    assert total == expected


@pytest.mark.version_2
def test_increment_round_first():
    game = GameLogic()
    rounds = game.round
    expected = 1
    assert rounds == expected


@pytest.mark.version_2
def test_increment_round_first():
    game = GameLogic()
    game.increment_round()
    rounds = game.round
    expected = 1
    assert rounds == expected
