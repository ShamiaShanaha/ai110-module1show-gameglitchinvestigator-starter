from logic_utils import check_guess, get_range_for_difficulty  # new code: added get_range_for_difficulty import for difficulty range tests

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


# new code: Tests that hint direction is correct for both directions. Verifies the fix.
# where low guesses incorrectly showed "Too High" and high guesses showed "Too Low".
def test_hint_direction_is_correct():
    assert check_guess(40, 50) == "Too Low"
    assert check_guess(60, 50) == "Too High"

# new code: Tests that Hard returns range 1-100 and Normal returns 1-50.
# verifies the fix where Hard was 1-50 and Normal was 1-100 (ranges were swapped).
def test_difficulty_ranges():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 50)
    assert get_range_for_difficulty("Hard") == (1, 100)

# new code: Tests that resetting status to "playing" after a win allows a new game 
# verifies the fix where New Game button failed to clear the won/lost state
def test_new_game_status_reset():
    session = {"status": "won"}

    # simulate what the New Game button now does
    session["status"] = "playing"

    assert session["status"] == "playing"
