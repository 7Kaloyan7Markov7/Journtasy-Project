from scripts.handlers.handler import Handler


class MenuHandler(Handler):
    def handle(self, game):
        current_scene = game.scene_manager.current_scene
        left_click_position = game.input_manager.left_click_position

        self.start_game_event(game, current_scene, left_click_position)
        self.quit_game_menu_event(game, current_scene, left_click_position)

    def start_game_event(self, game, scene, left_click_position):
        if left_click_position is False:
            return

        if scene.start_button.is_clicked(left_click_position):
            self.open_character_selection_event(game)

    def open_character_selection_event(self, game):
        game.scene_manager.open_character_selection()

    def quit_game_menu_event(self, game, scene, left_click_position):
        if left_click_position is False:
            return

        if scene.exit_button.is_clicked(left_click_position):
            game.running = False