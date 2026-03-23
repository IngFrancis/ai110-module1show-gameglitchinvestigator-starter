## 2. How did you use AI as a teammate?

### Correct AI Suggestion

**What the AI suggested:**
Copilot correctly identified that the hint messages in `check_guess()` were reversed —
when `guess > secret`, the code was returning "Go HIGHER!" instead of "Go LOWER!".
It also identified that on even-numbered attempts, `secret` was being converted to a
string, causing lexicographic comparisons instead of numeric ones.

**Was it correct?**
Yes. I verified this by checking the debug panel during gameplay — the secret was 30,
I guessed 47, and the hint said "Go HIGHER!" which was clearly wrong.

**How I verified it:**
I fixed the hint messages in `check_guess()` and ran the pytest tests
`test_hint_says_go_lower_when_guess_too_high` and
`test_hint_says_go_higher_when_guess_too_low`. Both passed, confirming the fix.

### Incorrect/Misleading AI Suggestion

**What the AI suggested:**
Copilot suggested adding input validation and `.copy()` for `getPurchaseHistory()`
as refinements, and also suggested using `round(total, 2)` for floating point
precision in score calculations.

**Was it correct?**
Misleading — these suggestions added unnecessary complexity not required by the spec.
The activity explicitly said to avoid over-engineering and keep implementations simple.

**How I verified it:**
I compared each suggestion against the spec and UML diagram. Since none of these
additions were listed as requirements, I ignored them and kept the code minimal.

---

## 3. Debugging and Testing Your Fixes

### Bug 1: Attempts Counter

- **How I found it:** The debug panel showed `Attempts: 0` even after multiple guesses,
  and the display always showed "Attempts left: 8".
- **How I fixed it:** Changed `st.session_state.attempts = 1` to `= 0` in `app.py`.
- **How I verified it:** Played the game and confirmed the counter decreased correctly
  after each guess.

### Bug 2: Reversed Hints

- **How I found it:** Guessed 47 with secret 30 and got "Go HIGHER!" — clearly wrong.
- **How I fixed it:** Swapped the hint messages in `check_guess()` in `logic_utils.py`
  and removed the string conversion in `app.py`.
- **How I verified it:** Ran `pytest tests/test_game_logic.py -v` — all 8 tests passed.

### Bug 3: Score Never Updates

- **How I found it:** Debug panel showed `Score: 0` throughout the entire game.
- **How I fixed it:** This was a cascading bug from Bug 2. Once Bug 2 was fixed,
  `update_score()` received correct outcomes and updated properly.
- **How I verified it:** Ran `test_score_updates_on_win` and
  `test_score_updates_on_too_low` — both passed.
