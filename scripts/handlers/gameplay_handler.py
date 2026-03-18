from scripts.handlers.handler import Handler
from scripts.enums.enums import Direction
import scripts.constants.constants as const


class GameplayHandler(Handler):
    def handle(self, game):
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