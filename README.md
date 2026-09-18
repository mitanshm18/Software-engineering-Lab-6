# Software Engineering Assignment VI
## Open-Source Code Refactoring

**Original Project:** Battleship
**Original Repository URL:** https://github.com/gbrough/battleship
**Refactored Repository URL:** https://github.com/mitanshm18/Software-engineering-Lab-6
**Programming Language:** Python

### Code Smell Audit
1. **Duplicate Code:** `place_ships` function repeated identical logic for placing ships horizontally and vertically for both the player and the computer.
2. **Magic Numbers:** The hardcoded number `8` was used throughout the codebase for the board dimensions.
3. **Complex Conditional/Loop:** `user_input` had a massive `while True` and `try-except` structure (Cyclomatic Complexity = 18) just to validate input.
4. **Poor Naming:** `column` was used in `count_hit_ships` to refer to an individual cell, not a column index.

### Refactoring & Testing
- **Coverage:** Reached 78% statement coverage using pytest.
- **Extract Method:** Abstracted duplicate placement loops into `place_ship_on_board()`.
- **Magic Numbers:** Extracted `BOARD_SIZE = 8` to handle grid bounds mathematically instead of hardcoding.
- **Simplify Loops:** Created a reusable `get_valid_input()` helper which dropped `user_input` complexity from 18 to 4.
- **Rename Variable:** Renamed `column` to `cell`.

### How to Run
```bash
python battleship.py
```

### How to Run Tests
```bash
pip install pytest pytest-cov
python -m pytest --cov=battleship test_battleship.py
```