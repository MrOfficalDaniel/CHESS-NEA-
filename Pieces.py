import os



class Pieces:
    def __init__(self, name, color, value, texture=None, texture_rect=None):
        self.name = name
        self.color = color
        value_sign = 1 if color == "white" else -1
        self.value = value * value_sign
        self.validmoves = []
        self.moved = False
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect

    def set_texture(self, size=80):
        filename = f"{self.color}_{self.name.lower()}.png"
        self.texture = os.path.join(
            f'assets/images/imgs-{size}px/{self.color}_{self.name}.png')

    def add_valid_moves(self, moves):
        self.validmoves.append(moves)

class Pawn(Pieces):
    def __init__(self, color):
        self.dir = -1 if color == "white" else 1
        super().__init__("Pawn", color, 1)

class Knight(Pieces):
    def __init__(self, color):
        super().__init__("Knight", color, 3)

class Bishop(Pieces):
    def __init__(self, color):
        super().__init__("Bishop", color, 3)

class Queen(Pieces):
    def __init__(self, color):
        super().__init__("Queen", color, 9)

class King(Pieces):
    def __init__(self, color):
        super().__init__("King", color, 0)
        

class Rook(Pieces):
    def __init__(self, color):
        super().__init__("Rook", color, 5)