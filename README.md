# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the fixed app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: _"How do I keep a variable from resetting in Streamlit when I click a button?"_
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

### Game Purpose

Game Glitch Investigator is a number guessing game built with Streamlit. The player
tries to guess a secret number within a limited number of attempts. After each guess,
the game provides a hint ("Go HIGHER!" or "Go LOWER!") to guide the player toward
the correct answer. The game tracks attempts and score across difficulty levels
(Easy, Normal, Hard).

### Bugs Found

**Bug 1: Attempts Counter Not Counting Down**

- The attempts counter was initialized to `1` instead of `0`, causing it to display
  7 on first load and never count down after guesses.
- Fixed by changing `st.session_state.attempts = 1` to `= 0` in `app.py`.

**Bug 2: Hints Were Reversed**

- The hint messages in `check_guess()` were swapped — "Go HIGHER!" was shown when
  the guess was too high, and "Go LOWER!" when it was too low.
- Additionally, on even-numbered attempts, the secret number was converted to a string,
  causing incorrect lexicographic comparisons instead of numeric ones.
- Fixed by swapping the hint messages in `logic_utils.py` and removing the string
  conversion in `app.py`.

**Bug 3: Score Never Updated**

- The score stayed at 0 throughout the game because Bug 2 caused `check_guess()` to
  return wrong outcomes, which fed incorrect data to `update_score()`.
- Fixed as a cascading result of fixing Bug 2.

### Fixes Applied

- Refactored all game logic (`check_guess`, `parse_guess`, `get_range_for_difficulty`,
  `update_score`) from `app.py` into `logic_utils.py`.
- Fixed attempts initialization, reversed hints, and string conversion bug.
- Added 8 pytest tests in `tests/test_game_logic.py` to verify all fixes.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]

## 🧪 Tests

Run the test suite with:

```bash
python -m pytest tests/test_game_logic.py -v
```

All 8 tests pass:

- `test_winning_guess`
- `test_guess_too_high`
- `test_guess_too_low`
- `test_hint_says_go_lower_when_guess_too_high`
- `test_hint_says_go_higher_when_guess_too_low`
- `test_check_guess_uses_numeric_comparison`
- `test_score_updates_on_win`
- `test_score_updates_on_too_low`

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
