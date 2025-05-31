import random

import pygame

from script.assets import load_animations


class Player:
    def __init__(self, screen_width, screen_height):
        self.animations = load_animations()
        self.current_state = 'idle'
        self.player_anim_count = 0
        self.animation_speed = 500
        self.last_frame_time = pygame.time.get_ticks()


        self.player_x = (screen_width - 100) // 2
        self.player_y = (screen_height - 100) // 2
        self.move_speed = 5


        self.scale_factor = 0.4

    def change_state(self):
        states = ['idle', 'walk_right', 'walk_left']
        self.current_state = random.choice(states)

    def update(self):
        current_time = pygame.time.get_ticks()

        if self.current_state == 'walk_right':
            self.player_x += self.move_speed
        elif self.current_state == 'walk_left':
            self.player_x -= self.move_speed


        if self.player_x < 0:
            self.player_x = 0
        elif self.player_x > pygame.display.Info().current_w - 100:
            self.player_x = pygame.display.Info().current_w - 100

        if current_time - self.last_frame_time > self.animation_speed:
            self.player_anim_count = (self.player_anim_count + 1) % len(self.animations[self.current_state])
            self.last_frame_time = current_time

        if random.randint(1, 100) < 5:
            self.change_state()

    def draw(self, screen):
        current_animation = self.animations[self.current_state]
        current_frame = current_animation[self.player_anim_count]


        original_width, original_height = current_frame.get_size()


        new_width = int(original_width * self.scale_factor)
        new_height = int(original_height * self.scale_factor)


        scaled_frame = pygame.transform.scale(current_frame, (new_width, new_height))


        screen.blit(scaled_frame, (self.player_x, self.player_y))
