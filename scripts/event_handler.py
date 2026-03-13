from input_manager import InputManager
import constants as const


class EventHandler:
    def pause_event(self, scene, input):
        if scene.scene_id == "gameplay" and input.pause_pressed():
            scene.pause_unpause()