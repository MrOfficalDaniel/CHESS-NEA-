import pygame
from const import *
from Boards_stuff import Board2
from dragger import dragger



class Board:
    def __init__(self, surface):
        self.surface = surface
        self.board = Board2()
        self.dragger = dragger()

    def show_board(self):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = white_color
                else:
                    color = green_color

                rect = (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(self.surface, color, rect)


    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                square = self.board.square[row][col]
                if square.has_piece():
                    piece = square.piece
                    img = pygame.image.load(piece.texture)
                    img_center = (
                        col * SQUARE_SIZE + SQUARE_SIZE // 2,
                        row * SQUARE_SIZE + SQUARE_SIZE // 2,
                    )
                    piece.texture_rect = img.get_rect(center=img_center)
                    surface.blit(img, piece.texture_rect)


        #timestamp - 1.25.40