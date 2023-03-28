import pytest
from ten_thousand.game_logic import GameLogic

pytestmark = [pytest.mark.version_1]


def test_single_five():
    actual = GameLogic.calculate_score((5,))
    expected = 50
    assert actual == expected


def test_single_one():
    actual = GameLogic.calculate_score((1,))
    expected = 100
    assert actual == expected


def test_two_fives():
    actual = GameLogic.calculate_score((5, 5))
    expected = 100
    assert actual == expected


def test_two_ones():
    actual = GameLogic.calculate_score((1, 1))
    expected = 200
    assert actual == expected


def test_one_and_five():
    actual = GameLogic.calculate_score((1, 5))
    expected = 150
    assert actual == expected


def test_zilch():
    actual = GameLogic.calculate_score((2,))
    expected = 0
    assert actual == expected


def test_three_fives():
    actual = GameLogic.calculate_score((5, 5, 5, 2, 2, 3))
    expected = 500
    assert actual == expected


def test_three_ones():
    actual = GameLogic.calculate_score((1, 1, 1, 2, 3, 4))
    expected = 1000
    assert actual == expected


def test_three_ones_and_a_five():
    actual = GameLogic.calculate_score((1, 1, 1, 5))
    expected = 1050
    assert actual == expected


def test_straight():
    actual = GameLogic.calculate_score((1, 6, 3, 2, 5, 4))
    # changed expected from 1500
    expected = 2000
    assert actual == expected


def test_three_of_a_kind():
    actual = GameLogic.calculate_score((2, 2, 2))
    expected = 200
    assert actual == expected


def test_four_of_a_kind():
    actual = GameLogic.calculate_score((2, 2, 2, 2))
    expected = 400
    assert actual == expected


def test_five_of_a_kind():
    actual = GameLogic.calculate_score((2, 2, 2, 2, 2))
    # changed expected from 600
    expected = 800
    assert actual == expected


def test_six_of_a_kind():
    actual = GameLogic.calculate_score((2, 2, 2, 2, 2, 2))
    # changed expected from 800
    expected = 1600
    assert actual == expected


def test_six_ones():
    actual = GameLogic.calculate_score((1, 1, 1, 1, 1, 1))
    # changed expected from 4000
    expected = 8000
    assert actual == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (tuple(), 0),
        ((1,), 100),
        ((1, 1), 200),
        ((1, 1, 1), 1000),
        ((1, 1, 1, 1), 2000),
        ((1, 1, 1, 1, 1), 4000),  # 3000
        ((1, 1, 1, 1, 1, 1), 8000),  # 8000
        ((2,), 0),
        ((2, 2), 0),
        ((2, 2, 2), 200),
        ((2, 2, 2, 2), 400),
        ((2, 2, 2, 2, 2), 800),  # 600
        ((2, 2, 2, 2, 2, 2), 1600),  # 800
        ((3,), 0),
        ((3, 3), 0),
        ((3, 3, 3), 300),
        ((3, 3, 3, 3), 600),
        ((3, 3, 3, 3, 3), 1200),  # 900
        ((3, 3, 3, 3, 3, 3), 2400),  # 1200
        ((4,), 0),
        ((4, 4), 0),
        ((4, 4, 4), 400),
        ((4, 4, 4, 4), 800),
        ((4, 4, 4, 4, 4), 1600),  # 1200
        ((4, 4, 4, 4, 4, 4), 3200),  # 1600
        ((5,), 50),
        ((5, 5), 100),
        ((5, 5, 5), 500),
        ((5, 5, 5, 5), 1000),
        ((5, 5, 5, 5, 5), 2000),  # 1500
        ((5, 5, 5, 5, 5, 5), 4000),  # 2000
        ((6,), 0),
        ((6, 6), 0),
        ((6, 6, 6), 600),
        ((6, 6, 6, 6), 1200),
        ((6, 6, 6, 6, 6), 2400),  # 1800
        ((6, 6, 6, 6, 6, 6), 4800),  # 2400
        ((1, 2, 3, 4, 5, 6), 2000),  # 1500
        ((2, 2, 3, 3, 4, 6), 0),
        ((2, 2, 3, 3, 6, 6), 1500),
        ((1, 1, 1, 2, 2, 2), 2400),  # 1200
        # *******LEFTOVER ONES TESTS
        ((4, 4, 4, 4, 1), 900),
        ((6, 6, 6, 1, 1), 800),
        # *******LEFTOVER FIVES TESTS
        ((3, 3, 3, 3, 3, 5), 1250),
        ((2, 2, 2, 5, 5), 300),
        # *******LEFTOVER FIVE AND ONES TEST
        ((2, 2, 2, 1, 5, 1), 450)
    ],
)
def test_all(test_input, expected):
    actual = GameLogic.calculate_score(test_input)
    assert actual == expected
