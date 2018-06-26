import math

import pygame

class Piece:
    black = pygame.Color(0, 0, 0, 255)
    white = pygame.Color(255,255,255,255)
    def __init__(self, own, pos):
        self.owner = own
        self.pos = pos
        
    def get_moves(self):
        return self.moves

    def move(self, diff):
        self.pos = tuple(map(sum, zip(self.pos, diff)))

    
        

class Rock(Piece):
    moves = [[(1,0)],[(1,0),(1,0)],
             [(-1,0)],[(-1,0),(-1,0)],
             [(0,1)],[(0,1),(0,1)],
             [(0,-1)],[(0,-1),(0,-1)]]
    
    def can_take(self, other): return isinstance(other, Scissor) and other.owner != self.owner

    def draw(self, surf, size):
        pygame.draw.circle(surf, Piece.black if self.owner == 0 else Piece.white,
                           (int(self.pos[0] * size[0] + size[0]/2),
                            int(self.pos[1] * size[1] + size[1]/2)),
                           math.ceil(min(size[0]/2,size[1]/2) * .8))

        pygame.draw.circle(surf, Piece.black if self.owner == 1 else Piece.white,
                           (int(self.pos[0] * size[0] + size[0]/2),
                            int(self.pos[1] * size[1] + size[1]/2)),
                           math.ceil(min(size[0]/2,size[1]/2) * .7))

class Paper(Piece):
    moves = [[(1,1)],[(1,1),(1,1)],
             [(-1,1)],[(-1,1),(-1,1)],
             [(1,-1)],[(1,-1),(1,-1)],
             [(-1,-1)],[(-1,-1),(-1,-1)]]
    
    def can_take(self, other): return isinstance(other, Rock) and other.owner != self.owner
    
    def draw(self, surf, size):
        pygame.draw.rect(surf, Piece.black if self.owner == 0 else Piece.white,
                           pygame.Rect(
                           (int(self.pos[0] * size[0] + size[0] * 0.1),
                            int(self.pos[1] * size[1] + size[1] * 0.1)),
                           (math.ceil(size[0] * 0.8), math.ceil(size[1] * 0.8))))
        
        pygame.draw.rect(surf, Piece.black if self.owner == 1 else Piece.white,
                           pygame.Rect(
                           (int(self.pos[0] * size[0] + size[0] * 0.15),
                            int(self.pos[1] * size[1] + size[1] * 0.15)),
                           (math.ceil(size[0] * 0.7), math.ceil(size[1] * 0.7))))

class Scissor(Piece):
    moves = [[(1,2)],[(1,-2)],
             [(2, 1)],[(2, -1)],
             [(-2, 1)],[(-2, -1)],
             [(-1,2)],[(-1,-2)]]
    
    
    def can_take(self, other): return isinstance(other, Paper) and other.owner != self.owner

    def draw(self, surf, size):
        pygame.draw.polygon(surf, Piece.black if self.owner == 0 else Piece.white,
                           [(int(self.pos[0] * size[0] + size[0] * 0.5),
                            int(self.pos[1] * size[1] + size[1] * 0.1)),
                            (int(self.pos[0] * size[0] + size[0] * 0.1),
                             math.ceil(self.pos[1] * size[1] + size[1] *0.9)),
                            (math.ceil(self.pos[0] * size[0] + size[0] * 0.9),
                             math.ceil(self.pos[1] * size[1] + size[1] *0.9))])
        
        pygame.draw.polygon(surf, Piece.black if self.owner == 1 else Piece.white,
                           [(int(self.pos[0] * size[0] + size[0] * 0.5),
                            int(self.pos[1] * size[1] + size[1] * 0.15)),
                            (int(self.pos[0] * size[0] + size[0] * 0.15),
                             math.ceil(self.pos[1] * size[1] + size[1] *0.85)),
                            (math.ceil(self.pos[0] * size[0] + size[0] * 0.85),
                             math.ceil(self.pos[1] * size[1] + size[1] *0.85))])
        
