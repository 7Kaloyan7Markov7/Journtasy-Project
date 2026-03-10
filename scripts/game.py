import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,600))
        self.clock = pygame.time.Clock()
        self.running = True

    def main_loop(self):
        self.load_assets()

        while self.running:
            self.input_handler()
            self.update()
            self.render() 
            self.clock .tick(60)

        pygame.quit()

    def input_handler(self): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def load_assets(self):
        ...

    def update(self):
        ...

    def render(self):
        ...

game = Game()
game.main_loop()