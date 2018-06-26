import pygame
import myBoard
import myTurn
from pygame.locals import *

class App:
    def __init__(self):
        self._running = True
        self._display_surf = True
        self.size = self.width, self.height = 400, 400
        self.board = myBoard.Board(self.size)
        self.turn = myTurn.Turn(self.board)

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(
            self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.turn.click(event.pos)

    def on_loop(self):
        pass

    def on_render(self):
        self.board.draw(self._display_surf)
        pygame.display.update()

    def on_cleanup(self):
        pygame.quit()
        
    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            #self._running = False
        self.on_cleanup()


if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
