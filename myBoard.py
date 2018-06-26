import pygame

import myPieces

class Board:
    def __init__(self, screen_size):
        self.size = self.width, self.height = 8, 8
        self.grid_size = screen_size[0] // self.width, screen_size[0] // self.height
        self.positions = [
            [None for x in range(self.height)]
                  for x in range(self.width)]
        self.highlights =  [
            [False for x in range(self.height)]
                  for x in range(self.width)]

    def setup(self):
        for i in range(8):
            self.place_piece(myPieces.Rock(0, (i, 0)), (i, 0))
            self.place_piece(myPieces.Scissor(0, (i, 1)), (i, 1))
            self.place_piece(myPieces.Paper(0, (i, 2)), (i, 2))
            self.place_piece(myPieces.Rock(1, (i, 7)), (i, 7))
            self.place_piece(myPieces.Scissor(1, (i, 6)), (i, 6))
            self.place_piece(myPieces.Paper(1, (i, 5)), (i, 5))

            
    def is_on_board(self, pos):
        return 0 <= pos[0] < self.width and 0 <= pos[1] < self.height

    def is_empty(self, pos):
        return self.is_on_board(pos) and self.positions[pos[0]][pos[1]] is None

    def get_piece(self, pos):
        return self.positions[pos[0]][pos[1]] if not self.is_empty(pos) else None

    def get_movable_positions(self, piece):
        positions = []
        
        for steps in piece.get_moves():
            x,y = piece.pos
            while len(steps) > 0:
                x += steps[0][0]
                y += steps[0][1]
                if not self.is_empty((x,y)) and len(steps) > 1:
                    break
                else:
                    steps = steps[1:]
            if len(steps) == 0 and self.is_on_board((x,y)) and (self.is_empty((x,y)) or piece.can_take(self.positions[x][y])):
                positions.append((x,y))

        return positions

                
    def can_move(self, piece):
        return len(self.get_movable_positions(piece)) > 0
    
    def place_piece(self, piece, pos):
        if not self.is_empty(pos):
            raise ValueError(str(pos) + " is not an empty position")
        elif piece is None:
            raise ValueError("Piece can not be None")
        else:
            self.positions[pos[0]][pos[1]] = piece

    def move_piece(self, piece, pos):
        if piece is None:
            raise ValueError("Piece can not be None")
        elif not pos in self.get_movable_positions(piece):
            raise ValueError("the piece cannot move to " + str(pos))
        else:
            self.positions[pos[0]][pos[1]] = piece
            self.positions[piece.pos[0]][piece.pos[1]] = None
            piece.pos = pos
        

    def highlight(self, positions):
        for y in range(self.height):
            for x in range(self.width):
                self.highlights[x][y] = False
        for x,y in positions:
            self.highlights[x][y] = True

    def is_highlighted(self, pos):
        return self.is_on_board(pos) and self.highlights[pos[0]][pos[1]]

    def get_all_owned_by(self, owner):
        pieces = []
        for y in range(self.height):
            for x in range(self.width):
                if not self.positions[x][y] is None and self.positions[x][y].owner == owner:
                    pieces.append(self.positions[x][y])
        return pieces

    def highlight_owned_by(self, owner):
        self.highlight([x.pos for x in self.get_all_owned_by(owner) if self.can_move(x)])

    def has_lost(self, player):
        types = set()
        for i in range(self.width):
            for j in range(self.height):
                piece = self.get_piece((i,j))
                if not piece is None and piece.owner == player:
                    types.add(piece.__class__)

        return len(types) < 3
        

    def draw(self, surf):
        
        for i in range(self.width):
            for j in range(self.height):
                c = 50 + 150 * ((1+i+j) % 2)
                r = c
                if self.highlights[i][j]:
                    r += 50
                surf.fill(pygame.Color(r, c, c, 255),
                          pygame.Rect(i*self.grid_size[0], j*self.grid_size[1], self.grid_size[0], self.grid_size[1]))
                
                if self.is_empty((i,j)) == False:
                    self.get_piece((i,j)).draw(surf, (self.grid_size[0], self.grid_size[1]))
