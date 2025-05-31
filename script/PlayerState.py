import random
import pygame
from script.assets import load_animations

class PlayerState:
    def __init__(self, screen_width, screen_height):
        self.animations = load_animations()
        self.current_state = 'idle'
        self.player_x = (screen_width - 100) // 2
        self.player_y = (screen_height - 100) // 2
        self.move_speed = 5
        self.idle_start_time = 1

        # Инициализация показателей
        self.happiness = 75  # Уровень счастья (от 0 до 100)
        self.hunger = 100     # Уровень голода (от 0 до 100)
        self.energy = 100     # Уровень бодрости (от 0 до 100)

    def change_state(self, new_state):
        if new_state in ['idle', 'walk_right', 'walk_left']:
            self.current_state = new_state
            if new_state == 'idle':
                self.idle_start_time = pygame.time.get_ticks()  # Запоминаем время начала состояния idle

    def update(self):
        current_time = pygame.time.get_ticks()

        # Если уровень счастья полон, устанавливаем состояние idle
        if self.happiness == 100:
            self.change_state('idle')

            # Проверяем, сколько времени прошло в состоянии idle
            if self.idle_start_time is not None and (current_time - self.idle_start_time) > 30000:  # Более 30 секунд
                # Случайно выбираем направление движения (влево или вправо)
                if random.choice([True, False]):
                    self.change_state('walk_right')
                else:
                    self.change_state('walk_left')
                self.idle_start_time = None  # Сбрасываем время начала состояния idle

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.change_state('walk_right')
            self.player_x += self.move_speed
        elif keys[pygame.K_LEFT]:
            self.change_state('walk_left')
            self.player_x -= self.move_speed
        else:
            if not (self.current_state in ['walk_right', 'walk_left']):
                self.change_state('idle')

    def get_position(self):
        return self.player_x, self.player_y

    def get_status(self):
        return {
            'happiness': self.happiness,
            'hunger': self.hunger,
            'energy': self.energy,
        }
