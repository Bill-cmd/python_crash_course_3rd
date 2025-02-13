import sys
import pygame

class BlueSky():

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Bule Sky")

        self.bg_color = (135, 206, 235)

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
        self.screen.fill(self.bg_color)
        pygame.display.flip()



bs = BlueSky()
bs.run_game()

