import sys
import pygame
from settings import Settings
from bird import Bird

class BlueBird():
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Bule Bird")

        self.bird = Bird(self)


    def run_game(self):
        while True:
            self._check_events()
            self.update_screen()
            self.clock.tick(60)

    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.bird.blitme()

        pygame.display.flip()



bb = BlueBird()
bb.run_game()

