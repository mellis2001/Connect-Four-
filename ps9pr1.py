#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 18:45:02 2019

@author: mellis
"""

class Board: 
    """creates connect 4 board""" 
    
    def __init__(self, height, width): 
        """a constructor for Board objects"""
        self.height = height
        self.width = width 
        self.slots = [[' '] * self.width for row in range(self.height)]
        
    def __repr__(self): 
        """ Returns a string representation for a Board object.
    """
        s = ''         # begin with an empty string

    # add one row of slots at a time
        for row in range(self.height):
                s += '|'   # one vertical bar at the start of the row

                for col in range(self.width):
                    s += self.slots[row][col] + '|'

                s += '\n'  # newline at the end of the row

    # Add code here for the hyphens at the bottom of the board
        for col in range(self.width):
            s += '--' 
        s += '-'
        s += '\n'
       
    # and the numbers underneath it.
        for col in range(self.width):
            
            s += ' ' + str(col % 10)
             
    
        return s
    
    def add_checker(self, checker, col):
        """ adds specified checker to correct column col
    """
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)

    # put the rest of the method here
        row = self.height - 1  
        while self.slots[row][col] != ' ' :  
            row -= 1
            if row == -1: 
                row = -1
                break
        self.slots[row][col] = checker
        
    def reset(self): 
        """clears the board of checkers""" 
        self.__init__(self.height, self.width)
    
    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
        checkers in those columns of the called Board object, 
        starting with 'X'.
    """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

        # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'
    
    def can_add_to(self, col): 
        """ runs through col if is a possible input return True else False"""
        if col < 0 or col > self.width - 1:
            return False 
        elif self.slots[0][col] == 'X' or self.slots[0][col] == 'O':
            return False
        else: 
            return True
    def is_full(self): 
        """checks if board is competely full""" 
        full_num = self.width * self.height
        num = 0 
        for row in range(self.height):
            for col in range(self.width): 
                if self.slots[row][col] == 'X' or self.slots[row][col] == 'O': 
                    num += 1 
        if num == full_num: 
            return True 
        else: 
            return False 
    
    def remove_checker(self, col): 
        """removes the top checker from col of Board""" 
        row = 0 
        bottom = self.height - 1 
        if self.slots[bottom][col] == ' ':
            self.slots[bottom][col] == self.slots[row][col]
        else: 
            while self.slots[row][col] != 'X' and self.slots[row][col] != 'O':
                row += 1

             
                 
        self.slots[row][col] = ' '
                
    
    def is_horizontal_win(self, checker) : 
        """ Checks for a horizontal win for the specified checker.
    """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                self.slots[row][col + 1] == checker and \
                self.slots[row][col + 2] == checker and \
                self.slots[row][col + 3] == checker:
                   return True

    # if we make it here, there were no horizontal wins
        return False
    
    def is_vertical_win(self, checker): 
        """checks for vertical win for the specified checker""" 
        for row in range(self.height - 3):
            for col in range(self.width):
                if self.slots[row][col] == checker and\
                self.slots[row + 1][col] == checker and \
                self.slots[row + 2][col] == checker and \
                self.slots[row + 3][col] == checker: 
                    return True 
        return False 
    def is_down_diagonal_win(self, checker): 
        """checks for down diagonal win for the specified checker""" 
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and\
                self.slots[row + 1][col + 1] == checker and \
                self.slots[row + 2][col + 2] == checker and \
                self.slots[row + 3][col + 3] == checker: 
                    return True 
        return False 
    def is_up_diagonal_win(self,checker): 
        """ checks for up diagonal win for the specified checker""" 
        for row in range(3 , self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and\
                self.slots[row - 1][col + 1] == checker and \
                self.slots[row - 2][col + 2] == checker and \
                self.slots[row - 3][col + 3] == checker: 
                    return True 
        return False  
    
    def is_win_for(self, checker): 
        """checks if there if checkers are in a row""" 
        horizontal = self.is_horizontal_win(checker)
        vertical = self.is_vertical_win(checker)
        down_diag = self.is_down_diagonal_win(checker)
        up_diag = self.is_up_diagonal_win(checker)
        if horizontal or vertical or down_diag or up_diag == True:
            return True
        
        return False
         
            

            
    