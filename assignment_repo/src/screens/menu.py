from src.game import Game, set_game

class MenuScreen:
    def __init__(self, app):
        self.app = app
        self.game = Game(player=None, sounds=self.app.sounds)
        set_game(self.game)

    def update(self, input_state):
        if input_state.start_pressed:
            from src.screens.play import PlayScreen
            self.app.change_screen(PlayScreen(self.app))
            return

        # animate background like original menu
        self.game.update(None)

    def draw(self, screen):
        self.game.draw(screen)

        # title overlay like original
        screen.blit("title", (0, 0))

        anim_frame = min(((self.game.timer + 40) % 160) // 4, 9)
        screen.blit("space" + str(anim_frame), (130, 280))
