import random
'''
            ---CLI remake of the classic game Mastermind---
GOAL: Guess the correct 4 color code, in order, in as few turns as possible.
'''
COLORS = ["B", "G", "R", "O", "W", "Y"]
TRIES = 10
CODE_LENGTH = 4

def generate_code(code_length, colors) -> list[str]:
    """
    Create a random code of specified length using a list of characters
    representing colors.
    """
    code = random.choices(colors, k=code_length)
    return code

def guess_code(code_length, colors, guess=False) -> list[str]:
    """
    Get the players guess and return that guess as a list of characters.
    """
    while True:
        # Get the players guess and split thier choices into a list
        if not guess:
            guess = input("Guess: ").upper().split(' ')
        # Ask player to guess again if the number of choices was invalid
        if len(guess) != code_length:
            print(f"\nYou must guess {code_length} colors\n")
            return False
        # Ask player to guess again if they gave invalid input
        if set(guess).issubset(colors) == False:
            print(f"\nInvalid color.\nValid colors are: {colors}.\nTry again\n")
            return False
        return guess

def check_code(code, guess) -> tuple[int]:
    """
    Comparing the players guess to the "answer" code. Returns a tuple of 
    integers containing how many colors are out of position, and how many 
    colors are in position.
    """
    correct_colors = {color:0 for color in guess}
    correct_positions = 0
    # Iterate the players guess colors and the correct code colors at the same time
    for guess_color, real_color in zip(guess, code):
        # Check which colors that player guessed are in the correct position
        if guess_color == real_color:
            correct_positions += 1
        # Check how many colors player guessed correctly but are in wrong position
        elif guess_color in code and guess_color != real_color:
            correct_colors[guess_color] += 1
    # Return total colors guessed correctly, and how many are in position
    return sum(correct_colors.values()), correct_positions

def run(code, turns_remaining) -> None:
    """
    Games main loop. Runs until player guesses the code correctly
    or until player runs out of turns.
    """
    # Run while player has turns remaining
    while turns_remaining > 0:
        print(f"Turns Left: {turns_remaining}")
        # Get the players guess
        guess = False
        while guess == False:
            guess = guess_code(code_length=CODE_LENGTH, colors=COLORS)
        # If player guesses the code
        if guess == code:
            print(f"*** YOU WIN! ***")
            exit()
        # If players guess is incorrect
        else:
            # Get how many colors are out of position, and how many are in position
            incorrect_positions, correct_positions = check_code(code=code, guess=guess)
            print(f"\tColors Correct: {incorrect_positions}")
            print(f"\tColors in Position: {correct_positions}\n")
            print(f"{'-'*20}\n")
            # Subtract 1 turn from total turns left
            turns_remaining -= 1         
    # Player ran out of turns
    print(f"YOU LOSE.... Code was: {code}")

if __name__ == "__main__":
    # Create code player should try and guess
    CODE = generate_code(colors=COLORS, code_length=CODE_LENGTH)
    run(code=CODE, turns_remaining=TRIES)