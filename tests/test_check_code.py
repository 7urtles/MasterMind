from mastermind import check_code, COLORS
import random
from copy import copy



def test_check_code_all_positions() -> None:
    """
    If input code and guess are the same correct position should be same as code length
    and correct_colors should be zero
    """
    code_length = random.randint(1,10)
    code = random.choices(COLORS, k=code_length)
    correct_colors, correct_positions = check_code(code=code, guess=code)
    assert correct_colors == 0
    assert correct_positions == code_length


def test_check_code_all_colors() -> None:
    """
    If all colors are correct but all postions are wrong then correct_colors value should be
    same as lenght of the code to be guessed and correct_positions should be zero
    """
    code_length = random.randint(1, len(COLORS))
    code = random.sample(COLORS, k=code_length)
    guess = copy(code)
    guess.insert(0,guess.pop())
    correct_colors, correct_positions = check_code(code=code, guess=guess)
    assert correct_colors == code_length
    assert correct_positions == 0