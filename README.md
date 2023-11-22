# TECHIN509B-TicTacToe

## Running Tests

To run the tests for the TicTacToe game, execute the following command:

```bash
python tests.py
```

### Test Functions Overview

The test suite in `tests.py` covers the following aspects of the TicTacToe game:

1. **Initial Empty Board Test**: Validates that the game starts with an empty board.
2. **Initialization Tests**:
   - **Two Human Players**: Ensures the game correctly initializes with two human players.
   - **Human and Bot Player**: Confirms the game can be initialized with one human and one bot player.
3. **Player Symbols Assignment**: Checks that players are assigned unique symbols (X or O).
4. **Alternate Turns**: Verifies that after one player plays, the turn switches to the other player.
5. **Winning Conditions and Draws**:
   - **Winning Conditions**: Tests for all possible winning scenarios (row, column, diagonal).
   - **Draw Detection**: Ensures that draw games are correctly identified when no player wins.
6. **Valid Moves**: Confirms players can only play in unoccupied spots on the board.
7. **Winner Detection**: Assesses the accurate detection of the game winner, if one exists.
