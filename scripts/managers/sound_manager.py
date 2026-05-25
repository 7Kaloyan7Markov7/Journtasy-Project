from pygame import mixer

import scripts.config.constants as const

class SoundManager:
    def __init__(self):
        mixer.init(frequency=44100, size=-16, channels=2, buffer=512)
        sounds = {}

    def _load_sounds(self):
        for sound_name, sound_path in const.SOUNDS:
            SoundManager.sounds[sound_name] = mixer.Sound(sound_path)

    @staticmethod
    def play_sound(sound):
        SoundManager.sounds[sound].play()
    
    @staticmethod
    def play_music():
        mixer.music.load(const.MUSIC2_PATH)
        mixer.music.play()
        