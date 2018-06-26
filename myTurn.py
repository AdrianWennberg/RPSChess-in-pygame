import pygame
import myBoard

class Turn:
    def __init__(self, board):
        self.board = board
        self.setup()
        
    def setup(self):
        self.board.setup()
        self.player, self.other = 0, 1
        self.selected = None
        self.highlight()

    def highlight(self):
        if self.selected is None:
            self.board.highlight_owned_by(self.player)
        else:
            self.board.highlight(self.board.get_movable_positions(self.selected))

    def select(self, pos):
        self.selected = self.board.get_piece(pos)


    def click(self, pos):
        pos = pos[0] // self.board.grid_size[0] , pos[1] // self.board.grid_size[1]

        if not self.board.is_highlighted(pos):
            return
        elif self.selected == None:
            self.selected = self.board.get_piece(pos)
            self.highlight()
        else:
            self.board.move_piece(self.selected, pos)
            self.player, self.other = self.other, self.player
            if self.board.has_lost(self.player):
                print("player " +str( self.other + 1) + " has won")
               
            self.selected = None
            self.highlight()

        print(self.player)
