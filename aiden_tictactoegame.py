# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 13:36:45 2022

@author: 18016
"""

class TicTacToeGame:
    def __init__(self):
        self.state = [[" "," "," "], [" "," "," "], [" "," "," "]]
    def print_state(self):
        for row in self.state:
            print ("!".join(row))
            if row is not self.state[-1]:
                print ("------")
                
        print ("....................................")

            
    def mark(self, row, col, symbol):
        if self.state[row][col] == " ":
            self.state[row][col] = symbol
            return True
        else:
            return False
    def get_winner(self):
        pass
    def is_tie(self):
        pass
    
if __name__ == "__main__":
    t = TicTacToeGame()
    t.mark(0,0,"X")
    t.print_state()
    t.mark(1,1,"O")
    t.print_state()
    t.mark(2,2,"X")
    t.print_state()
    