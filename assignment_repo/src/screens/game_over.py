from src.game import draw_status, set_game

class GameOverScreen:
    def __init__(self, app, game):
        self.app = app
        self.game = game
        set_game(self.game)

    def update(self, input_state):
        # Return to menu on SPACE edge
        if input_state.fire_pressed:
            from src.screens.menu import MenuScreen
            self.app.change_screen(MenuScreen(self.app))
            return

    def draw(self, screen):
        self.game.draw(screen)
        draw_status(screen)
        screen.blit("over", (0, 0))
