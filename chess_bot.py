import random
import time
from abc import ABC, abstractmethod

import chess


class ChessBotClass(ABC):
    @abstractmethod
    def __call__(self, board_fen: str) -> chess.Move:
        pass


class ChessBot(ChessBotClass):
    def __init__(self):
        self.piece_values = {
            chess.PAWN: 100,
            chess.KNIGHT: 320,
            chess.BISHOP: 330,
            chess.ROOK: 500,
            chess.QUEEN: 900,
            chess.KING: 20000,
        }
        self.transposition_table = {}
        self.max_evaluations = 1000  # Limit as per tournament rule
        self.eval_count = 0  # Track evaluations
        self.piece_square_table = {
            chess.PAWN: [
                0,
                5,
                10,
                -20,
                -20,
                10,
                5,
                0,
                0,
                10,
                20,
                -10,
                -10,
                20,
                10,
                0,
                5,
                10,
                30,
                0,
                0,
                30,
                10,
                5,
                10,
                20,
                40,
                30,
                30,
                40,
                20,
                10,
                10,
                20,
                40,
                30,
                30,
                40,
                20,
                10,
                5,
                10,
                30,
                0,
                0,
                30,
                10,
                5,
                0,
                10,
                20,
                -10,
                -10,
                20,
                10,
                0,
                0,
                5,
                10,
                -20,
                -20,
                10,
                5,
                0,
            ],
            chess.KNIGHT: [
                -50,
                -40,
                -30,
                -30,
                -30,
                -30,
                -40,
                -50,
                -40,
                -20,
                0,
                5,
                5,
                0,
                -20,
                -40,
                -30,
                5,
                10,
                15,
                15,
                10,
                5,
                -30,
                -30,
                0,
                15,
                20,
                20,
                15,
                0,
                -30,
                -30,
                5,
                15,
                20,
                20,
                15,
                5,
                -30,
                -30,
                0,
                10,
                15,
                15,
                10,
                0,
                -30,
                -40,
                -20,
                0,
                0,
                0,
                0,
                -20,
                -40,
                -50,
                -40,
                -30,
                -30,
                -30,
                -30,
                -40,
                -50,
            ],
            chess.BISHOP: [
                -20,
                -10,
                -10,
                -10,
                -10,
                -10,
                -10,
                -20,
                -10,
                5,
                0,
                0,
                0,
                0,
                5,
                -10,
                -10,
                10,
                10,
                10,
                10,
                10,
                10,
                -10,
                -10,
                0,
                10,
                10,
                10,
                10,
                0,
                -10,
                -10,
                5,
                5,
                10,
                10,
                5,
                5,
                -10,
                -10,
                0,
                5,
                10,
                10,
                5,
                0,
                -10,
                -10,
                0,
                0,
                0,
                0,
                0,
                0,
                -10,
                -20,
                -10,
                -10,
                -10,
                -10,
                -10,
                -10,
                -20,
            ],
            chess.ROOK: [
                0,
                0,
                5,
                10,
                10,
                5,
                0,
                0,
                -5,
                0,
                0,
                0,
                0,
                0,
                0,
                -5,
                -5,
                0,
                0,
                0,
                0,
                0,
                0,
                -5,
                -5,
                0,
                0,
                0,
                0,
                0,
                0,
                -5,
                -5,
                0,
                0,
                0,
                0,
                0,
                0,
                -5,
                -5,
                0,
                0,
                0,
                0,
                0,
                0,
                -5,
                5,
                10,
                10,
                10,
                10,
                10,
                10,
                5,
                0,
                0,
                5,
                10,
                10,
                5,
                0,
                0,
            ],
            chess.QUEEN: [
                -20,
                -10,
                -10,
                -5,
                -5,
                -10,
                -10,
                -20,
                -10,
                0,
                5,
                0,
                0,
                0,
                0,
                -10,
                -10,
                5,
                5,
                5,
                5,
                5,
                0,
                -10,
                0,
                0,
                5,
                5,
                5,
                5,
                0,
                0,
                -5,
                0,
                5,
                5,
                5,
                5,
                0,
                -5,
                -10,
                0,
                5,
                5,
                5,
                5,
                0,
                -10,
                -10,
                0,
                0,
                0,
                0,
                0,
                0,
                -10,
                -20,
                -10,
                -10,
                -5,
                -5,
                -10,
                -10,
                -20,
            ],
            chess.KING: [
                20,
                30,
                10,
                0,
                0,
                10,
                30,
                20,
                20,
                20,
                0,
                0,
                0,
                0,
                20,
                20,
                -10,
                -20,
                -20,
                -30,
                -30,
                -20,
                -20,
                -10,
                -20,
                -30,
                -30,
                -40,
                -40,
                -30,
                -30,
                -20,
                -30,
                -40,
                -40,
                -50,
                -50,
                -40,
                -40,
                -30,
                -30,
                -40,
                -40,
                -50,
                -50,
                -40,
                -40,
                -30,
                -30,
                -40,
                -40,
                -50,
                -50,
                -40,
                -40,
                -30,
                -30,
                -40,
                -40,
                -50,
                -50,
                -40,
                -40,
                -30,
            ],
        }

    def __call__(self, board_fen: str) -> chess.Move:
        board = chess.Board(board_fen)
        legal_moves = list(board.legal_moves)
        if not legal_moves:
            return None  # No legal move means checkmate or stalemate.

        self.eval_count = 0  # Reset count each move
        best_move = random.choice(legal_moves)  # Always have a fallback move
        depth = 1

        while self.eval_count < self.max_evaluations:
            try:
                move = max(
                    legal_moves,
                    key=lambda move: self.evaluate_move(board, move),
                    default=best_move,
                )
                if self.eval_count >= self.max_evaluations:
                    break
                best_move = move
                depth += 1
            except Exception as e:
                print(f"Error in move selection: {e}")
                break  # Ensure the bot does not crash

        return best_move

    def evaluate_move(self, board, move):
        if self.eval_count >= self.max_evaluations:
            return 0

        board.push(move)
        self.eval_count += 1
        value = -self.minimax(board, 3, -float("inf"), float("inf"), False)
        board.pop()
        return value

    def minimax(self, board, depth, alpha, beta, maximizing):
        if (
            self.eval_count >= self.max_evaluations
            or depth == 0
            or board.is_game_over()
        ):
            return self.evaluate_position(board)

        legal_moves = sorted(
            board.legal_moves, key=lambda m: self.move_ordering(board, m), reverse=True
        )

        if maximizing:
            value = -float("inf")
            for move in legal_moves:
                board.push(move)
                self.eval_count += 1
                value = max(value, self.minimax(board, depth - 1, alpha, beta, False))
                board.pop()
                alpha = max(alpha, value)
                if beta <= alpha or self.eval_count >= self.max_evaluations:
                    break
            return value
        else:
            value = float("inf")
            for move in legal_moves:
                board.push(move)
                self.eval_count += 1
                value = min(value, self.minimax(board, depth - 1, alpha, beta, True))
                board.pop()
                beta = min(beta, value)
                if beta <= alpha or self.eval_count >= self.max_evaluations:
                    break
            return value

    def evaluate_position(self, board):
        if board.is_checkmate():
            return -20000 if board.turn else 20000
        if board.is_stalemate() or board.is_insufficient_material():
            return 0

        score = 0
        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if piece:
                value = self.piece_values[piece.piece_type]
                score += value if piece.color else -value
        return score

    def move_ordering(self, board, move):
        if board.is_capture(move):
            piece = board.piece_at(move.to_square)
            return self.piece_values.get(piece.piece_type, 0) if piece else 0
        elif board.gives_check(move):
            return 50
        elif board.is_castling(move):
            return 40
        elif move.promotion:
            return 1000
        return 0
