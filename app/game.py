# Wave 1
# Add your Wave 1 functions here

# generate_code 
# - takes no arguments  
# - returns a list of 4 letters
# - each letter must be one of: R, O, Y, G, B, P
# - letters can be repeated
# - the list must be generated randomly
import random

def generate_code():
    colors = ['R', 'O', 'Y', 'G', 'B', 'P']
    return [random.choice(colors) for _ in range(4)]

def validate_guess(guess):
    valid_colors = {'R', 'O', 'Y', 'G', 'B', 'P'}
    if len(guess) != 4:
        return False
    for char in guess:
        if char.upper() not in valid_colors:
            return False
    return True

def check_code_guessed(guess, code):
    """Return True if guess matches code (case-insensitive), otherwise False.

    Both guess and code are expected to be 4-element lists of letters.
    """
    # Basic validation: must be lists of length 4
    if not (isinstance(guess, list) and isinstance(code, list)):
        return False
    if len(guess) != 4 or len(code) != 4:
        return False

    # Compare elements case-insensitively to be forgiving of lowercase input
    return all(str(g).upper() == str(c).upper() for g, c in zip(guess, code))

# Wave 2
# Add your Wave 2 functions here

# Wave 3
# Add your Wave 3 functions here
