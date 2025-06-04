import pygame

def load_assets(asset_type):
    if asset_type == 'background':
        return pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/images/background.jpg')


def load_animations():
    animations = {
        'idle': [
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/idle/IdleAnim1.png'),
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/idle/IdleAnim2.png'),
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/idle/IdleAnim3.png'),
        ],
        'walk_right': [
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/walk_right/WalkAnimRight1.png'),
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/walk_right/WalkAnimRight2.png'),
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/walk_right/WalkAnimRight3.png'),
        ],
        'walk_left': [
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/walk_left/WalkAnimLeft1.png'),
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/walk_left/WalkAnimLeft2.png'),
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/walk_left/WalkAnimLeft3.png'),
        ],
        'refuse': [
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/.png'),
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/.png'),
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/.png'),
        ],
        'sleep': [
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/.png'),
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/.png'),
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/.png'),
        ],
        'eat': [
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/.png'),
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/.png'),
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/.png'),
        ],
        'play': [
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/.png'),
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/.png'),
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/.png'),
        ]
    }
    return animations
