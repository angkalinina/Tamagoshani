import pygame

SPRITE_SIZE = 100


def load_backgrounds():
    def load(path):
        return pygame.image.load(path)

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
        image = pygame.image.load(image_path)
        return pygame.transform.scale(image, (SPRITE_SIZE, SPRITE_SIZE))

    return {
        'idle': [
            scale('animations/idle/IdleAnim1.png'),
            scale('animations/idle/IdleAnim2.png'),
            scale('animations/idle/IdleAnim3.png'),
        ],
        'walk_right': [
            scale('animations/walk_right/WalkAnimRight1.png'),
            scale('animations/walk_right/WalkAnimRight2.png'),
            scale('animations/walk_right/WalkAnimRight3.png'),
        ],
        'walk_left': [
            scale('animations/walk_left/WalkAnimLeft1.png'),
            scale('animations/walk_left/WalkAnimLeft2.png'),
            scale('animations/walk_left/WalkAnimLeft3.png'),
        ],
        'refuse': [
            scale('animations/refuse/RefuseAnim1.png'),
            scale('animations/refuse/RefuseAnim2.png'),
            scale('animations/refuse/RefuseAnim3.png'),
            scale('animations/refuse/RefuseAnim4.png'),
        ],
        'sleep': [
            scale('animations/sleep/SleepAnim1.png'),
            scale('animations/sleep/SleepAnim2.png'),
            scale('animations/sleep/SleepAnim3.png'),
            scale('animations/sleep/SleepAnim4.png'),
        ],
        'eat': [
            scale(f'animations/eat/EatAnim{i}.png') for i in range(1, 11)
        ],
        'play': [
            scale(f'animations/play_left/PlayAnim{i}.png') for i in range(1, 7)
        ] + [
            scale(f'animations/play_right/PlayAnim{i}.png') for i in range(1, 7)
        ]
    }
