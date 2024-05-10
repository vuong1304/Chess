import random
from board import Board

CHECKMATE = 1000 

class AI:
    def __init__(self):
        self.square = None
        self.squares_with_pieces = []
        self.piece = None
        self.board = Board()
        
    def get_pieces(self):
        self.squares_with_pieces = []
        for row in self.board.squares:
            for square in row: 
                if square.piece != None and square.piece.color == 'black':
                    self.squares_with_pieces.append(square)
                    
    def find_best_move(self, game):
        score = 0
        bestMove = None
        for square in self.squares_with_pieces:
            self.board.calc_moves(square.piece, square.row, square.col, bool=True)
            for move in square.piece.moves:
                if self.move_score(move) > score:
                    score = self.move_score(move)
                    bestMove = move
                    self.piece = square.piece
        if score > 0: return bestMove
        else: 
            while True:
                square = random.choice(self.squares_with_pieces)
                if square.piece.moves == []:
                    continue
                else:
                    self.piece = square.piece
                    move = random.choice(square.piece.moves)
                    return move
            
    def move_score(self, move):
        if self.board.squares[move.final.row][move.final.col].has_piece():
            return self.board.squares[move.final.row][move.final.col].piece.value
        return 0
            
        
        
    