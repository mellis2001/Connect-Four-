#
# ps9pr3.py  (Problem Set 9, Problem 3)
#
# Playing the game 
#   

from ps9pr1 import Board
from ps9pr2 import Player
import random
    
def connect_four(p1, p2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: p1 and p2 are objects representing Connect Four
          players (objects of the Player class or a subclass of Player).
          One player should use 'X' checkers and the other should
          use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if p1.checker not in 'XO' or p2.checker not in 'XO' \
       or p1.checker == p2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    b = Board(6, 7)
    print(b)
    
    while True:
        if process_move(p1, b) == True:
            return b

        if process_move(p2, b) == True:
            return b
        
def process_move(p, b): 
    """takes player object whose move is process and board object""" 
    p.__repr__()
    print( p," 's turn" , end='')
    col = p.next_move(b)
    b.add_checker(p.checker,col)
    print()
    print(b)
    if b.is_win_for(p.checker) == True :
        print(p, end='')
        print(' wins in', p.num_moves, end='')
        print(' moves.')
        print('Congratulations!')
        return True 
    elif b.is_win_for(p.checker) == False and b.is_full() == True :
        print('Its a tie!')
        return True 
    else: 
        return False 
    
class RandomPlayer(Player): 
    def next_move(self, b):
        """overrides the next_move method, the next move is chosen at random"""
        self.num_moves += 1 
        open_col = []
        for c in range(b.width):
            if b.can_add_to(c) == True : 
                open_col += [c]
        return random.choice(open_col)


        
        
    
