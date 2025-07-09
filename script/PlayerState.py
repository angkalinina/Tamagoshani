from petcore.character import Tamagotchi
from assets import load_animations
from ui.resources import load_animations


class PlayerState:
    def __init__(self, screen_width, screen_height):
        self.pet = Tamagotchi(name="Tama_Pygame")  # вместо своих energy/hunger
        self.animations = load_animations()
        self.current_state = 'idle'
        self.sprite_size = 100
        self.player_x = (screen_width - self.sprite_size) // 2
        self.player_y = screen_height - self.sprite_size - 20
        self.move_speed = 5

    def update(self):
        self.pet.tick()

    def handle_input(self):
        pass

    def get_position(self):
        return self.player_x, self.player_y

    def get_status(self):
        return {
            'hunger': int(self.pet.hunger),
            'energy': int(self.pet.energy),
        }
