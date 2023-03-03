from mastermind import generate_code, COLORS
import random

def test_generate_code_default() -> None:
    code_length = random.randint(1,10)
    CODE = generate_code(colors=COLORS, code_length=code_length)
    assert code_length == len(CODE)
    assert set(CODE).issubset(COLORS)