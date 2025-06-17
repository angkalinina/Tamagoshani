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
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/refuse/RefuseAnim1.png'),
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/refuse/RefuseAnim2.png'),
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/refuse/RefuseAnim3.png'),
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/refuse/RefuseAnim4.png'),
        ],
        'sleep': [
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/sleep/SleepAnim1.png'),
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/sleep/SleepAnim2.png'),
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/sleep/SleepAnim3.png'),
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/sleep/SleepAnim4.png'),
        ],
        'eat': [
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/eat/EatAnim1.png'),
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/eat/EatAnim2.png'),
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/eat/EatAnim3.png'),
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/eat/EatAnim4.png'),
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/eat/EatAnim5.png'),
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/eat/EatAnim6.png'),
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/eat/EatAnim7.png'),
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/eat/EatAnim8.png'),
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/eat/EatAnim9.png'),
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/eat/EatAnim10.png'),
        ],
        'play': [
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/play_left/PlayAnim1.png'),
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/play_left/PlayAnim2.png'),
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/play_left/PlayAnim3.png'),
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/play_left/PlayAnim4.png'),
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/play_left/PlayAnim5.png'),
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/play_left/PlayAnim6.png'),
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/play_right/PlayAnim1.png'),
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/play_right/PlayAnim2.png'),
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/play_right/PlayAnim3.png'),
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/play_right/PlayAnim4.png'),
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/play_right/PlayAnim5.png'),
            pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/animations/play_right/PlayAnim6.png'),
        ]
    }
    return animations
