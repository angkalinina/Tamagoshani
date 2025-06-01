import pygame
from assets import load_assets
from PlayerState import PlayerState
from PlayerActions import PlayerActions


class Game:
    def __init__(self):

        pygame.init()


        self.clock = pygame.time.Clock()
        self.screen_width = pygame.display.Info().current_w
        self.screen_height = pygame.display.Info().current_h
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Shanezhka')


        self.background = load_assets('background')


        self.player_state = PlayerState(self.screen_width, self.screen_height)
        self.player_actions = PlayerActions(self.player_state)

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

        self.player_actions.update()
        self.player_state.update()
        self.player_state.handle_input()

    def render(self):
        self.screen.blit(self.background, (0, 0))


        pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()
