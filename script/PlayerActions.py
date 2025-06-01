import pygame
import random

class PlayerActions:
    def __init__(self, player_state):
        self.player_state = player_state
        self.idle_cycles = 0
        self.sleeping = False

    def eat(self):
        if self.player_state.hunger < 99:
            self.player_state.hunger += 30
            if self.player_state.hunger > 100:
                self.player_state.hunger = 100
            self.idle_cycles = 0
        else:
            self.refuse()

    def play(self):
        if self.player_state.energy > 30 and self.player_state.hunger > 30:

            self.idle_cycles = 0
        else:
            self.refuse()

    def sleep(self):
        if self.player_state.energy < 3 or self.player_state.hunger < 3:

            self.player_state.energy += 0.5
            self.player_state.hunger += 0.5
            if self.player_state.energy > 100:
                self.player_state.energy = 100
            if self.player_state.hunger > 100:
                self.player_state.hunger = 100
            self.sleeping = True
        elif 3 <= self.player_state.energy <= 40:

            self.player_state.energy += 0.5
            self.player_state.hunger += 0.5
            if self.player_state.energy > 100:
                self.player_state.energy = 100
            if self.player_state.hunger > 100:
                self.player_state.hunger = 100
            self.idle_cycles = 0
        elif self.player_state.energy > 40:
            self.refuse()

    def refuse(self):

        self.idle_cycles = 0

    def update(self):

        if not self.sleeping:
            if self.idle_cycles < 5:

                self.player_state.energy -= 0.1
                self.player_state.hunger -= 0.1
                if self.player_state.energy < 0:
                    self.player_state.energy = 0
                if self.player_state.hunger < 0:
                    self.player_state.hunger = 0
                self.idle_cycles += 1
            else:

                if random.choice([True, False]):
                    self.walk_right()
                else:
                    self.walk_left()

    def walk_right(self):

        self.player_state.energy -= 0.3
        if self.player_state.energy < 0:
            self.player_state.energy = 0

    def walk_left(self):

        self.player_state.energy -= 0.3
        if self.player_state.energy < 0:
            self.player_state.energy = 0
