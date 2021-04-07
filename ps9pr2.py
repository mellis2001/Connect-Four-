#
# ps9pr2.py  (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below
class Player(Board): 
    
    def __init__(self, checker):
        """returns string of objects""" 
        self.checker = checker 
        assert(checker == 'X' or checker == 'O')
        self.num_moves = 0 
    
    def __repr__(self):
        """ returns a string of Player object""" 
        s = 'Player' 
        if self.checker == 'X' :
            s += ' X'
        else: 
            s += ' O'
        return s 
        
       
    def opponent_checker(self): 
        """returns a string of the opponent's piece either x or o""" 
        s = ''
        if self.checker == 'X': 
            s += 'O' 
        else: 
            s += 'X'
        return s 
    
    def next_move(self, b): 
        """ using board object returns col that player wants to make next move
        and incriments total number of moves""" 
        self.num_moves += 1 
        
        while True: 
            col = int(input('Enter a column: '))
            if b.can_add_to(col) == True: 
                return col 
            else: 
                print('Try again!')
