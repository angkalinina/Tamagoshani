import pygame
import os

SPRITE_SIZE = 100

# Путь к корню проекта
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # /Tamagoshani

def resolve_path(relative_path):
    return os.path.join(BASE_DIR, "visual", relative_path)


def load_backgrounds():
    def load(path):
        full_path = resolve_path(path)
        return pygame.image.load(full_path)

    return {
        'dawn': load('images/background/background_dawn.png'),
        'morning': load('images/background/background_morning.png'),
        'day': load('images/background/background_day.png'),
        'twilight': load('images/background/background_twilight.png'),
        'night': load('images/background/background_night.png'),
        'predawn': load('images/background/background_predawn.png'),
    }


def load_animations():
    def scale(image_path):
        full_path = resolve_path(image_path)
        image = pygame.image.load(full_path)
        return pygame.transform.scale(image, (SPRITE_SIZE, SPRITE_SIZE))

    return {
        'idle': [scale(f'animations/idle/IdleAnim{i}.png') for i in range(1, 4)],
        'walk_right': [scale(f'animations/walk_right/WalkAnimRight{i}.png') for i in range(1, 4)],
        'walk_left': [scale(f'animations/walk_left/WalkAnimLeft{i}.png') for i in range(1, 4)],
        'refuse': [scale(f'animations/refuse/RefuseAnim{i}.png') for i in range(1, 5)],
        'sleep': [scale(f'animations/sleep/SleepAnim{i}.png') for i in range(1, 5)],
        'eat': [scale(f'animations/eat/EatAnim{i}.png') for i in range(1, 11)],
        'play': (
            [scale(f'animations/play_left/PlayAnim{i}.png') for i in range(1, 7)] +
            [scale(f'animations/play_right/PlayAnim{i}.png') for i in range(1, 7)]
        )
    }
