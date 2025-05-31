import pygame
from assets import load_assets
from PlayerState import PlayerState  # Импортируем класс PlayerState
from PlayerActions import PlayerActions  # Импортируем класс PlayerActions


class Game:
    def __init__(self):
        # Инициализация Pygame
        pygame.init()

        # Установка параметров экрана
        self.clock = pygame.time.Clock()
        self.screen_width = pygame.display.Info().current_w
        self.screen_height = pygame.display.Info().current_h
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Shanezhka')

        # Загрузка фона
        self.background = load_assets('background')

        # Инициализация состояния и действий игрока
        self.player_state = PlayerState(self.screen_width, self.screen_height)
        self.player_actions = PlayerActions(self.player_state)

    def run(self):
        running = True
        while running:
            running = self.handle_events()
            if running:
                self.update()
                self.render()
            self.clock.tick(60)  # Ограничение частоты кадров

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False  # Выход из игры
        return True

    def update(self):
        # Обновление состояния и действий игрока
        self.player_actions.update()
        self.player_state.update()
        self.player_state.handle_input()

    def render(self):
        # Отрисовка фона
        self.screen.blit(self.background, (0, 0))


        pygame.display.update()  # Обновление экрана


if __name__ == "__main__":
    game = Game()  # Создание экземпляра игры
    game.run()  # Запуск игры
    pygame.quit()  # Завершение работы Pygame
