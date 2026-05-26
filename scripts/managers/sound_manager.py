from pygame import mixer

import scripts.config.constants as const

mixer.init(frequency=44100, size=-16, channels=2, buffer=512)

class SoundManager:
    sounds = {}

    @staticmethod
    def load_sounds():
        for sound_name, sound_path in const.SOUNDS.items():
            SoundManager.sounds[sound_name] = mixer.Sound(sound_path)

    @staticmethod
    def pause_music():
        mixer.music.pause()

    @staticmethod
    def unpause_music():
        mixer.music.unpause()

    @staticmethod
    def stop_music():
        mixer.music.fadeout(1)

    @staticmethod
    def play_sound(sound):
        SoundManager.sounds[sound].play()
    
    @staticmethod
    def play_music():
        mixer.music.load(const.MUSIC2_PATH)
        mixer.music.play()
        