import pygame
from const import *


class dragger:

    def __init__(self,):
        self.piece = None
        self.dragging = False
        self.mouseX = 0
        self.mouseY = 0
        self.inital_row = 0
        self.inital_col = 0
    #blit method which is used to update the position of the piece being dragged
    
    def update_blit(self, surface):

        #text
        self.piece.set_texture(size=120)
        texture = self.piece.texture

        #img
        img =  pygame.image.load(texture)

        #rect
        img_center = (self.mouseX, self.mouseY)
        self.piece.rect = img.get_rect(center=img_center)

        #blit
        surface.blit(img, self.piece.rect)

#other methods used in the main game loop
    def update_mouse(self, pos):
        self.mouseX, self.mouseY = pos #where pos is a tuple of the mouse position (x, y)

    def save_inital(self, pos):
        self.inital_row = pos[1] // SQUARE_SIZE
        self.inital_col = pos[0] // SQUARE_SIZE

    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True

    def undrag_piece(self):
        self.piece = None
        self.dragging = False