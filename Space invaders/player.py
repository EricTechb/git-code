from arcade import Sprite

class Player(Sprite):
    def __init__(self, x, y):
        super().__init__("assets/spaceship.png", image_x=0, image_y=0, image_width=72, image_height=72)

        self.center_x = x
        self.center_y = y

    def move_left(self):
        self.change_x = -3
    
    def move_right(self):
        self.change_x = 3

    def stop(self):
        self.change_x = 0