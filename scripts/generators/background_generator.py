from random import choice

from scripts.building_blocks.background import Background
from scripts.generators.generator import Generator
from scripts.config.constants import BACKGROUND_IDS


class BackgroundGenerator(Generator):
    def generate(self):
        return Background(choice(BACKGROUND_IDS))