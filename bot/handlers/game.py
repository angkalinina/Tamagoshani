import pygame
from ui.player_state import PlayerState
from system.time_manager import get_time_of_day
from ui.resources import load_backgrounds


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


class Game:
    def __init__(self):
        pygame.init()
        self.screen_width = 360
        self.screen_height = 640
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Shanezhka')

        self.backgrounds = load_backgrounds()

        self.player_state = PlayerState(self.screen_width, self.screen_height)

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 28)
        self.state = 'menu'  # стартовое состояние

    def run(self):
        running = True
        while running:
            if self.state == 'menu':
                running = self.handle_menu_events()
                self.render_menu()
            elif self.state == 'game':
                running = handle_events()
                if running:
                    self.update()
                    self.render_game()
            self.clock.tick(60)

    # ========== MENU ==========
    def handle_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 80 <= x <= 280:
                    if 150 <= y <= 190:
                        self.state = 'game'
                    elif 200 <= y <= 240:
                        self.state = 'game'
                    elif 250 <= y <= 290:
                        print("Настройки — в разработке")
                    elif 300 <= y <= 340:
                        print("Об игре — в разработке")
        return True

    def render_menu(self):
        self.screen.fill((30, 30, 30))
        self.draw_button("Новая игра", 150)
        self.draw_button("Продолжить", 200)
        self.draw_button("Настройки", 250)
        self.draw_button("Об игре", 300)
        pygame.display.update()

    def draw_button(self, text, y):
        pygame.draw.rect(self.screen, (70, 70, 70), (80, y, 200, 40), border_radius=10)
        label = self.font.render(text, True, (255, 255, 255))
        self.screen.blit(label, (180 - label.get_width() // 2, y + 10))

    # ========== GAME ==========
    def update(self):

        self.player_state.update()
        self.player_state.handle_input()

    def render_game(self):
        time_of_day = get_time_of_day()
        raw_background = self.backgrounds.get(time_of_day, self.backgrounds['day'])
        bg_width, bg_height = raw_background.get_size()
        scale_ratio = min(self.screen_width / bg_width, self.screen_height / bg_height)
        scaled_width = int(bg_width * scale_ratio)
        scaled_height = int(bg_height * scale_ratio)
        background = pygame.transform.scale(raw_background, (scaled_width, scaled_height))
        x_offset = (self.screen_width - scaled_width) // 2
        y_offset = (self.screen_height - scaled_height) // 2
        self.screen.blit(background, (x_offset, y_offset))

        current_state = self.player_state.current_state
        animations = self.player_state.animations
        frame = animations.get(current_state, animations['idle'])[0]
        x, y = self.player_state.get_position()
        self.screen.blit(frame, (x, y))

        # Индикаторы
        status = self.player_state.get_status()
        self.draw_stat_bar("Энергия", status["energy"], 10, 10, (0, 180, 255))
        self.draw_stat_bar("Голод", status["hunger"], 10, 40, (255, 180, 0))

        pygame.display.update()

    def draw_stat_bar(self, label, value, x, y, color):
        max_width = 200
        height = 20
        filled = int((value / 100) * max_width)

        # Фон полоски
        pygame.draw.rect(self.screen, (50, 50, 50), (x, y, max_width, height), border_radius=4)
        # Заполненная часть
        pygame.draw.rect(self.screen, color, (x, y, filled, height), border_radius=4)
        # Текст
        text = self.font.render(f"{label}: {int(value)}", True, (255, 255, 255))
        self.screen.blit(text, (x + max_width + 10, y + 2))

def update(self):
    self.player_state.update()
    self.player_state.handle_input()