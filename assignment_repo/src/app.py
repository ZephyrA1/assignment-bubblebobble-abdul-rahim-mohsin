from src.input import InputManager
from src.screens.menu import MenuScreen

class App:
    """
    Owns the current screen.
    All screen switching must go through change_screen(...) (assignment requirement).
    """
    def __init__(self):
        self.input_manager = InputManager()
        self.screen = MenuScreen(self)

    def change_screen(self, new_screen):
        self.screen = new_screen

    def update(self):
        input_state = self.input_manager.capture()
        self.screen.update(input_state)

    def draw(self):
        self.screen.draw()
