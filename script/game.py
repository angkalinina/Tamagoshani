import pygame
from player import Player
from assets import load_assets


class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.screen_width = pygame.display.Info().current_w
        self.screen_height = pygame.display.Info().current_h
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Shanezhka')

        self.background = load_assets('background')
        self.player = Player(self.screen_width, self.screen_height)

    def run(self):
        running = True
        while running:
            running = self.handle_events()
            if running:
                self.update()
                self.render()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    def update(self):
        self.player.update()

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.player.draw(self.screen)
        pygame.display.update()
