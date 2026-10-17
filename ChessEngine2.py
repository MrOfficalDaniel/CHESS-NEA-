
import pygame
import sys

from const import *
from MainGame import *

from MainGame import Board



class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Chess Game")
        self.game = Board(self.screen) 

        self.dragger = self.game.dragger  
        self.board = self.game.board  
    def mainloop(self):


     while True:
            self.screen.fill((0, 0, 0))
            self.game.show_board()
            self.game.show_pieces(self.screen)

            for event in pygame.event.get():

               #for clicking on the pieces
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.dragger.update_mouse(event.pos)

                    clicked_row = self.dragger.mouseY // SQUARE_SIZE
                    clicked_col = self.dragger.mouseX // SQUARE_SIZE

                    if self.board.square[clicked_row][clicked_col].has_piece():
                        piece = self.board.square[clicked_row][clicked_col].piece
                        self.dragger.save_inital(event.pos)
                        self.dragger.drag_piece(piece)


                
                elif event.type == pygame.MOUSEMOTION:
                   if self.dragger.dragging:
                       self.dragger.update_mouse(event.pos) 
                       self.dragger.update_blit(self.screen)
                
                
                #for releasing the pieces
                elif event.type == pygame.MOUSEBUTTONUP:
                   self.dragger.undrag_piece()

            


                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


def run():
    main = Main()
    main.mainloop()

