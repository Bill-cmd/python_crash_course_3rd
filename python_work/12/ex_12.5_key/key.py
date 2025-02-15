import sys
import pygame

class Key:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((1200, 800))
        self.display = pygame.display.set_caption("Key")

        self.bg_color = (255, 255, 255)

    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)

    def _update_screen(self):
        self.screen.fill(self.bg_color)
        pygame.display.flip()

if __name__ == '__main__':
    key = Key()
    key.run_game()
