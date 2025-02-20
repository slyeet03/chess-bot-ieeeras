import random

import chess

from chess_bot import ChessBot


def play_game():
    board = chess.Board()
    bot = ChessBot()
    move_count = 0  # Track total moves

    while not board.is_game_over():
        move_count += 1  # Increment move count each turn

        if board.turn:  # White's turn (bot)
            move = bot(board.fen())
            print(f"Bot plays: {move}")
        else:  # Black's turn (random moves)
            move = random.choice(list(board.legal_moves))
            print(f"Random opponent plays: {move}")

        board.push(move)
        print(board)
        print("\n")

    result = board.outcome().result()
    return result, move_count


def main():
    num_matches = 20
    bot_wins = 0
    bot_losses = 0
    draws = 0
    total_moves = 0

    for i in range(num_matches):
        print(f"Match {i + 1}:")
        result, move_count = play_game()
        total_moves += move_count

        if result == "1-0":
            bot_wins += 1
        elif result == "0-1":
            bot_losses += 1
        else:
            draws += 1

    avg_moves = total_moves / num_matches

    print(f"Bot Wins: {bot_wins}")
    print(f"Bot Losses: {bot_losses}")
    print(f"Draws: {draws}")
    print(f"Average Moves per Match: {avg_moves:.2f}")


if __name__ == "__main__":
    main()
