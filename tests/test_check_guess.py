from mastermind import guess_code, CODE_LENGTH, COLORS
import random

def test_guess_code_default() -> None:
    guess = random.choices(COLORS, k=CODE_LENGTH)
    assert guess_code(code_length=CODE_LENGTH, colors=COLORS, guess=guess) != False

def test_guess_code_length_too_long() -> None:
    guess = random.choices(COLORS, k=CODE_LENGTH+1)
    assert guess_code(code_length=CODE_LENGTH, colors=COLORS, guess=guess) == False

def test_guess_code_length_too_short() -> None:
    guess = random.choices(COLORS, k=CODE_LENGTH-1)
    assert guess_code(code_length=CODE_LENGTH, colors=COLORS, guess=guess) == False

def test_guess_code_invalid_choice() -> None:
    guess = random.choices(COLORS, k=CODE_LENGTH)
    guess[0] = 'i'
    assert guess_code(code_length=CODE_LENGTH, colors=COLORS, guess=guess) == False