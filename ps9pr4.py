#
# ps9pr4.py  (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four   
#

import random  
from ps9pr3 import *

class AIPlayer(Player): 
    def __init__(self, checker, tiebreak, lookahead):
        """ initializes tiebreak and lookahead
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead 
    
    def __repr__(self): 
        """ returns the player string, tiebreaking strategy, and lookahead""" 
        s = 'Player' 
        if self.checker == 'X' :
            s += ' X' 
        else: 
            s += ' O'
        if self.tiebreak == 'LEFT' :
            s += ' (LEFT' 
        elif self.tiebreak == 'RIGHT' :
            s += ' (RIGHT'
        else: 
            s += ' (RANDOM' 
        if self.lookahead >= 0 :
            s += ', ' + str(self.lookahead) + ')'
        return s 
    def max_score_column(self, scores): 
        """ returns the index of the col with the maximum score""" 
        score_list = []
        for s in range(len(scores)):
            if scores[s] == max(scores):
                score_list += [s] 
        
        if self.tiebreak == 'LEFT' :
            return score_list[0]
        elif self.tiebreak == 'RIGHT' :
            return score_list[-1]
        else: 
            return random.choice(score_list)
        
        
    def scores_for(self, b): 
        """ MUST return a list of scores- one for each column""" 
        scores = [50] * b.width
        for col in range(b.width): 
            if b.can_add_to(col) == False: 
                scores[col] = -1 
            elif b.is_win_for(self.checker) == True:
                scores[col] = 100 
            elif b.is_win_for(self.opponent_checker()) == True :
                scores[col] = 0 
            elif self.lookahead == 0: 
                scores[col] = 50 
            else: 
                b.add_checker(self.checker, col)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1 )
                opp_scores = opponent.scores_for(b)
                scores[col] = 100 - max(opp_scores)
                b.remove_checker(col)
                    
        return scores
    
    def next_move(self, b): 
        """ returns the AI's best judgment of the best possible move""" 
        self.num_moves += 1 
        scores = self.max_score_column(self.scores_for(b))
        return scores
    
        
        