from scripts.handlers.handler import Handler


class MenuHandler(Handler):
    def handle(self, game):
        ...

    def quit_game_menu_event(self, game, scene, user_click_position):
        if scene.exit_button.is_clicked(user_click_position):
            game.running = False    