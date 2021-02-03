import chess

class State(object):
    def __init__(self):
        self.board = chess.Board()

    def value(self):
        #TODO: add neural network here
        return 1

    def edges(self):
        return list(self.board.legal_moves)

    def serialize(self):
        # 257 bit according to readme
        pass
    
if __name__ == "__main__":
    s = State()
    print(s.edges())
