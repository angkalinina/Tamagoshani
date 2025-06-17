import random
import pygame
from assets import load_animations


class PlayerState:
    def __init__(self, screen_width, screen_height):
        self.animations = load_animations()
        self.current_state = 'idle'
        self.player_x = (screen_width - 100) // 2
        self.player_y = (screen_height - 100) // 2
        self.move_speed = 5
        self.idle_start_time = 0
        self.hunger = 100
        self.energy = 100

    def change_state(self, new_state):
        if new_state in ['idle', 'walk_right', 'walk_left', 'eat', 'sleep', 'play', 'refuse']:
            self.current_state = new_state
            if new_state == 'idle':
                self.idle_start_time = pygame.time.get_ticks()

    def update(self):
        self.update_stats()
        if self.current_state == 'idle' and pygame.time.get_ticks() - self.idle_start_time > 5000:
            self.change_state(random.choice(['walk_right', 'walk_left']))

    def update_stats(self):
        state_effects = {
            'idle': (-0.1, -0.1),
            'walk_right': (-0.3, -0.3),
            'walk_left': (-0.3, -0.3),
            'eat': (30, 10),
            'sleep': (0.5 if self.energy < 3 and self.hunger < 3 else 0, 0.5 if self.energy < 3 and self.hunger < 3 else 0)
        }

        hunger_change, energy_change = state_effects.get(self.current_state, (0, 0))
        self.adjust_stats(hunger_change, energy_change)

        if (self.energy < 3 or self.hunger < 3) and self.current_state in ['idle', 'walk_right', 'walk_left']:
            self.change_state('sleep')

    def adjust_stats(self, hunger_change, energy_change):
        self.hunger = max(0, min(100, self.hunger + hunger_change))
        self.energy = max(0, min(100, self.energy + energy_change))

    def handle_input(self):
        keys = pygame.key.get_pressed()
        actions = {
            pygame.K_RIGHT: ('walk_right', self.move_speed),
            pygame.K_LEFT: ('walk_left', -self.move_speed),
            pygame.K_e: ('eat', None),
            pygame.K_s: ('sleep' if 3 <= self.energy <= 40 else 'refuse', None),
            pygame.K_p: ('play' if self.energy > 30 and self.hunger > 30 else 'refuse', None)
        }

        for key, (action, delta_x) in actions.items():
            if keys[key]:
                if action in ['walk_right', 'walk_left']:
                    self.move(action, delta_x)
                else:
                    self.change_state(action)
                break

    def move(self, direction, delta_x):
        if self.energy > 3 and self.hunger > 3:
            self.change_state(direction)
            self.player_x += delta_x
        else:
            self.change_state('refuse')

    def get_position(self):
        return self.player_x, self.player_y

    def get_status(self):
        return {
            'hunger': int(self.hunger),
            'energy': int(self.energy),
        }
