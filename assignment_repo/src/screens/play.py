from src.game import Game, Player, draw_status, set_game

class PlayScreen:
    def __init__(self, app):
        self.app = app
        self.game = Game(Player(), sounds=self.app.sounds)
        set_game(self.game)

    def update(self, input_state):
        # optional pause screen
        if input_state.pause_pressed:
            from src.screens.pause import PauseScreen
            self.app.change_screen(PauseScreen(self.app, self))
            return

        if self.game.player.lives < 0:
            self.game.play_sound("over")
            from src.screens.game_over import GameOverScreen
            self.app.change_screen(GameOverScreen(self.app, self.game))
            return

        self.game.update(input_state)

    def draw(self, screen):
        self.game.draw(screen)
        draw_status(screen)
