from enums import Direction
import constants as const


class EventHandler:
    def pause_event(self, scene, user_input):
        if user_input.pause_pressed:
            scene.pause()

    def choosing_character_event(self, scene, user_input):
        if scene.knight_button.is_clicked(user_input):
            return const.KNIGHT_ID

        if scene.boxer_button.is_clicked(user_input):
            return const.BOXER_ID

        if scene.wizard_button.is_clicked(user_input):
            return const.WIZARD_ID

        if scene.monk_button.is_clicked(user_input):
            return const.MONK_ID

        if scene.killer_button.is_clicked(user_input):
            return const.KILLER_ID

        if scene.caveman_button.is_clicked(user_input):
            return const.CAVEMAN_ID

        return None

    def start_game_event(self, scene, user_input):
        ...

    def quit_game_event(self, scene, user_input):
        ...

    def quit_game_menu_event(self, scene, user_input):
        ...

    def player_stepped_bounds_event(self, player):
        if player.position.x <= const.SCREEN_LEFT_BOUNDARY:
            player.position.x = const.SCREEN_RIGHT_BOUNDARY - player.width
            self.room_transition_event(Direction.LEFT)

        elif player.position.x >= const.SCREEN_RIGHT_BOUNDARY - player.width:
            player.position.x = const.SCREEN_LEFT_BOUNDARY
            self.room_transition_event(Direction.RIGHT)

        elif player.position.y <= const.SCREEN_UPPER_BOUNDARY:
            player.position.y = const.SCREEN_LOWER_BOUNDARY - player.height
            self.room_transition_event(Direction.UP)

        elif player.position.y >= const.SCREEN_LOWER_BOUNDARY - player.height:
            player.position.y = const.SCREEN_UPPER_BOUNDARY
            self.room_transition_event(Direction.DOWN)

    def room_transition_event(self, dungeon_manager, direction):
        dungeon_manager.transition_to_new_room(direction)

    def handle_main_menu(self, game):
        ...

    def handle_character_selection(self, game):
        ...

    def handle_gameplay(self, game):
        self.player_stepped_bounds_event(game.scene_manager.scene.room.player)

    def handle(self, game):
        if game.scene_manager.current_scene.scene_id == const.MAIN_MENU_ID:
            self.handle_main_menu(game)

        if game.scene_manager.current_scene.scene_id == const.CHARACTER_SELECTION_ID:
            self.handle_character_selection(game)

        if game.scene_manager.current_scene.scene_id == const.GAME_SCENE_ID:
            self.handle_gameplay(game)