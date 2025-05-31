import pygame

class PlayerActions:
    def __init__(self, player_state):
        self.player_state = player_state
        self.last_feed_time = pygame.time.get_ticks()  # Время последнего кормления
        self.last_play_time = pygame.time.get_ticks()   # Время последней игры
        self.last_pet_time = pygame.time.get_ticks()    # Время последнего поглаживания

    def feed(self):
        if self.player_state.hunger < 100:
            self.player_state.hunger += 20
            if self.player_state.hunger > 100:
                self.player_state.hunger = 100
            self.last_feed_time = pygame.time.get_ticks()

    def pet(self):
        if self.player_state.happiness < 100:
            self.player_state.happiness += 5
            if self.player_state.happiness > 100:
                self.player_state.happiness = 100
            self.last_pet_time = pygame.time.get_ticks()

    def play(self):
        if self.player_state.happiness < 100:
            self.player_state.happiness += 10
            if self.player_state.happiness > 100:
                self.player_state.happiness = 100
            self.last_play_time = pygame.time.get_ticks()

    def sleep(self):
        if self.player_state.energy < 100:
            self.player_state.energy += 30
            if self.player_state.energy > 100:
                self.player_state.energy = 100

    def update(self):
        current_time = pygame.time.get_ticks()

        # Обновление уровня голода и бодрости со временем
        time_since_feed = current_time - self.last_feed_time
        time_since_play = current_time - self.last_play_time

        # Уменьшение голода со временем
        if time_since_feed > 5000:  # Каждые 5 секунд уменьшаем голод
            self.player_state.hunger -= 1
            if self.player_state.hunger < 0:
                self.player_state.hunger = 0

        # Уменьшение бодрости со временем
        if time_since_play > 3000:  # Каждые 3 секунды уменьшаем энергию
            self.player_state.energy -= 1
            if self.player_state.energy < 0:
                self.player_state.energy = 0
