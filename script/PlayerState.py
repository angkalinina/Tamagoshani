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
        self.idle_start_time = 0


        self.hunger = 100
        self.energy = 100

    def change_state(self, new_state):
        if new_state in ['idle', 'walk_right', 'walk_left', 'eat', 'sleep', 'play', 'refuse']:
            self.current_state = new_state
            if new_state == 'idle':
                self.idle_start_time = pygame.time.get_ticks()

    def update(self):
        current_time = pygame.time.get_ticks()


        if self.current_state == 'idle':
            self.hunger -= 0.1
            self.energy -= 0.1


            if self.energy < 3 or self.hunger < 3:
                self.change_state('sleep')


            if (current_time - self.idle_start_time) > 5000:
                self.change_state(random.choice(['walk_right', 'walk_left']))

        elif self.current_state in ['walk_right', 'walk_left']:
            self.hunger -= 0.3
            self.energy -= 0.3

        elif self.current_state == 'eat':
            self.hunger += 30
            self.energy += 10
            if self.hunger > 100:
                self.hunger = 100
            if self.energy > 100:
                self.energy = 100

        elif self.current_state == 'sleep':
            if self.energy < 3 and self.hunger < 3:

                self.hunger += 0.5
                self.energy += 0.5
                if self.hunger > 100:
                    self.hunger = 100
                if self.energy > 100:
                    self.energy = 100


        if not pygame.key.get_pressed():
            if not (self.current_state in ['walk_right', 'walk_left']):
                self.change_state('idle')

    def handle_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            if self.energy > 3 and self.hunger > 3:
                self.change_state('walk_right')
                self.player_x += self.move_speed
            else:
                self.change_state('refuse')

        elif keys[pygame.K_LEFT]:
            if self.energy > 3 and self.hunger > 3:
                self.change_state('walk_left')
                self.player_x -= self.move_speed
            else:
                self.change_state('refuse')

        elif keys[pygame.K_e]:
            if self.hunger < 99:
                self.change_state('eat')
            else:
                self.change_state('refuse')

        elif keys[pygame.K_s]:
            if 3 <= self.energy <= 40:
                self.change_state('sleep')
            elif self.energy > 40:
                self.change_state('refuse')

        elif keys[pygame.K_p]:
            if self.energy > 30 and self.hunger > 30:
                self.change_state('play')
            else:
                self.change_state('refuse')

    def get_position(self):
        return self.player_x, self.player_y

    def get_status(self):
        return {

            'hunger': max(0, min(100, int(self.hunger))),
            'energy': max(0, min(100, int(self.energy))),
        }
