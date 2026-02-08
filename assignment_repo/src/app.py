from src.input import InputManager
from src.screens.menu import MenuScreen

class App:
    """
    Owns the current screen and builds InputState once per frame (Task B).
    """
    def __init__(self, sounds):
        self.sounds = sounds
        self.input_manager = InputManager()
        self.screen = MenuScreen(self)

    def change_screen(self, new_screen):
        self.screen = new_screen

    def update(self):
        input_state = self.input_manager.capture()  # ✅ centralized snapshot once per frame
        self.screen.update(input_state)

    def draw(self, screen):
        self.screen.draw(screen)
