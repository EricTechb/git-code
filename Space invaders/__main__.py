import arcade
from player import Player

class SpaceInvaders(arcade.Window):
    def __init__(self):
        super().__init__(1, 1, "Space Invaders", fullscreen=True)
        self.player = Player(self.width / 2, self.height * 0.1)

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.ESCAPE:
            arcade.close_window()
        if symbol == arcade.key.A:
            self.player.move_left()
        if symbol == arcade.key.D:
            self.player.move_right()

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.A:
            self.player.stop()
        if symbol == arcade.key.D:
            self.player.stop()

    def on_draw(self):
        arcade.start_render()
        self.player.draw()

    def on_update(self, time):
        self.player.update()

if __name__ == "__main__":
    from sys import argv
    from os import chdir

    chdir(argv[0].rpartition("/")[0])

    SpaceInvaders()
    arcade.run()