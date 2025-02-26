# Chess Bot Project - The Bots Gambit

A chess engine implementation for the IEEE RAS The Bots Gambit competition. This bot uses minimax algorithm with alpha-beta pruning and piece-square tables for position evaluation.

## Features

- Minimax algorithm with alpha-beta pruning
- Position evaluation using piece values and piece-square tables
- Move ordering for better alpha-beta pruning efficiency
- Transposition table for storing previously evaluated positions
- Interactive web-based visualization
- Automated testing against random moves

## Project Structure

- `chess_bot.py` - Main bot implementation
- `test_bot.py` - Test script for evaluating bot performance
- `chess_visualizer.py` - Web-based chess board visualizer
- `chess_viewer.html` - HTML template for the chess board visualization

## Requirements

- Python 3.7+
- python-chess library

To install the required packages:

```bash
pip install python-chess
```

## Usage

### Running the Bot Tests

To test the bot's performance against random moves:

```bash
python test_bot.py
```

This will run 300 matches and display statistics including:

- Number of wins
- Number of losses
- Number of draws
- Average moves per match

### Using the Visualizer

To view the chess board in a web interface:

```bash
python chess_visualizer.py
```

This will:

1. Start a local server
2. Open your default web browser
3. Display an interactive chess board
4. Allow you to make moves and reset the board

## Technical Details

### Bot Implementation

The chess bot uses several chess programming techniques:

1. **Piece Values**:

   - Pawn: 100
   - Knight: 320
   - Bishop: 330
   - Rook: 500
   - Queen: 900
   - King: 20000

2. **Position Evaluation**:

   - Uses piece-square tables for positional scoring
   - Evaluates material balance
   - Considers checkmate and stalemate positions

3. **Move Ordering**:

   - Prioritizes captures
   - Considers checks
   - Values castling moves
   - Promotes pawn promotions

4. **Search Algorithm**:
   - Implements minimax with alpha-beta pruning
   - Maintains evaluation count within tournament limits
   - Uses iterative deepening for time management

## Competition Rules Compliance

- Maintains evaluation count below 1000 per move
- Uses only standard Python chess library
- Implements required ChessBotClass interface

## License

MIT License

## Contributing

This project was developed by the team "We Can't Code" during the Bots Gambit by IEEE RAS. The team members are:

- [bhaskarjya](https://github.com/cwnorhino)
- [slyeet03](https://github.com/slyeet03)

## Acknowledgments

- IEEE RAS for hosting The Bots Gambit competition
- python-chess library developers
- chess.js for the web visualization
