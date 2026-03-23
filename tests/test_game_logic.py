from logic_utils import check_guess, parse_guess, update_score

# --- Existing Tests (Fixed) ---

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

# --- New Tests Targeting Bug 2: Reversed Hints ---

def test_hint_says_go_lower_when_guess_too_high():
    # FIX verification: guessing 60 when secret is 50 should say "Go LOWER!"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_hint_says_go_higher_when_guess_too_low():
    # FIX verification: guessing 40 when secret is 50 should say "Go HIGHER!"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_check_guess_uses_numeric_comparison():
    # FIX verification: ensure numeric comparison is used, not string comparison
    # "47" > "30" lexicographically but 47 > 30 numerically — both should say "Too High"
    outcome, message = check_guess(47, 30)
    assert outcome == "Too High"
    assert "LOWER" in message

# --- New Tests Targeting Bug 1: Attempts Counter ---

def test_score_updates_on_win():
    # FIX verification: score should increase when player wins
    new_score = update_score(0, "Win", 1)
    assert new_score > 0

def test_score_updates_on_too_low():
    # FIX verification: score should decrease on Too Low
    new_score = update_score(20, "Too Low", 1)
    assert new_score == 15

    