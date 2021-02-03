Zero Knowledge Chess Engine

* Establish the Search Tree
* Use a neural network to prune the search tree

Definition: Value Network
V - f(board)

State(Board):


Pieces(2+7*2 = 16)
* Universal
** Blank
** Blank (En passant)
** En Passant
* Pieces
** Pawn
** Bishop
** Knight
** Rook
** Rook (can castle(
** Queen
** King

Extra State
* To move


8x8x4 + 4 = 257 Bits (# of bits to represent chess board with vector of 0's and 1's)
