import pygame

SPRITE_SIZE = 100


def load_backgrounds():
    def load(path):
        return pygame.image.load(path)

    return {
        'dawn': load('C:/Users/angel/PycharmProjects/Tamagoshani/images/background/background_dawn.png'),
        'morning': load('C:/Users/angel/PycharmProjects/Tamagoshani/images/background/background_morning.png'),
        'day': load('C:/Users/angel/PycharmProjects/Tamagoshani/images/background/background_day.png'),
        'twilight': load('C:/Users/angel/PycharmProjects/Tamagoshani/images/background/background_twilight.png'),
        'night': load('C:/Users/angel/PycharmProjects/Tamagoshani/images/background/background_night.png'),
        'predawn': load('C:/Users/angel/PycharmProjects/Tamagoshani/images/background/background_predawn.png'),
    }


def load_animations():
    def scale(image_path):
        image = pygame.image.load(image_path)
        return pygame.transform.scale(image, (SPRITE_SIZE, SPRITE_SIZE))

    animations = {
        'idle': [
            scale('C:/Users/angel/PycharmProjects/Tamagoshani/animations/idle/IdleAnim1.png'),
            scale('C:/Users/angel/PycharmProjects/Tamagoshani/animations/idle/IdleAnim2.png'),
            scale('C:/Users/angel/PycharmProjects/Tamagoshani/animations/idle/IdleAnim3.png'),
        ],
        'walk_right': [
            scale('C:/Users/angel/PycharmProjects/Tamagoshani/animations/walk_right/WalkAnimRight1.png'),
            scale('C:/Users/angel/PycharmProjects/Tamagoshani/animations/walk_right/WalkAnimRight2.png'),
            scale('C:/Users/angel/PycharmProjects/Tamagoshani/animations/walk_right/WalkAnimRight3.png'),
        ],
        'walk_left': [
            scale('C:/Users/angel/PycharmProjects/Tamagoshani/animations/walk_left/WalkAnimLeft1.png'),
            scale('C:/Users/angel/PycharmProjects/Tamagoshani/animations/walk_left/WalkAnimLeft2.png'),
            scale('C:/Users/angel/PycharmProjects/Tamagoshani/animations/walk_left/WalkAnimLeft3.png'),
        ],
        'refuse': [
            scale('C:/Users/angel/PycharmProjects/Tamagoshani/animations/refuse/RefuseAnim1.png'),
            scale('C:/Users/angel/PycharmProjects/Tamagoshani/animations/refuse/RefuseAnim2.png'),
            scale('C:/Users/angel/PycharmProjects/Tamagoshani/animations/refuse/RefuseAnim3.png'),
            scale('C:/Users/angel/PycharmProjects/Tamagoshani/animations/refuse/RefuseAnim4.png'),
        ],
        'sleep': [
            scale('C:/Users/angel/PycharmProjects/Tamagoshani/animations/sleep/SleepAnim1.png'),
            scale('C:/Users/angel/PycharmProjects/Tamagoshani/animations/sleep/SleepAnim2.png'),
            scale('C:/Users/angel/PycharmProjects/Tamagoshani/animations/sleep/SleepAnim3.png'),
            scale('C:/Users/angel/PycharmProjects/Tamagoshani/animations/sleep/SleepAnim4.png'),
        ],
        'eat': [
            scale('C:/Users/angel/PycharmProjects/Tamagoshani/animations/eat/EatAnim1.png'),
            scale('C:/Users/angel/PycharmProjects/Tamagoshani/animations/eat/EatAnim2.png'),
            scale('C:/Users/angel/PycharmProjects/Tamagoshani/animations/eat/EatAnim3.png'),
            scale('C:/Users/angel/PycharmProjects/Tamagoshani/animations/eat/EatAnim4.png'),
            scale('C:/Users/angel/PycharmProjects/Tamagoshani/animations/eat/EatAnim5.png'),
            scale('C:/Users/angel/PycharmProjects/Tamagoshani/animations/eat/EatAnim6.png'),
            scale('C:/Users/angel/PycharmProjects/Tamagoshani/animations/eat/EatAnim7.png'),
            scale('C:/Users/angel/PycharmProjects/Tamagoshani/animations/eat/EatAnim8.png'),
            scale('C:/Users/angel/PycharmProjects/Tamagoshani/animations/eat/EatAnim9.png'),
            scale('C:/Users/angel/PycharmProjects/Tamagoshani/animations/eat/EatAnim10.png'),
        ],
        'play': [
            scale('C:/Users/angel/PycharmProjects/Tamagoshani/animations/play_left/PlayAnim1.png'),
            scale('C:/Users/angel/PycharmProjects/Tamagoshani/animations/play_left/PlayAnim2.png'),
            scale('C:/Users/angel/PycharmProjects/Tamagoshani/animations/play_left/PlayAnim3.png'),
            scale('C:/Users/angel/PycharmProjects/Tamagoshani/animations/play_left/PlayAnim4.png'),
            scale('C:/Users/angel/PycharmProjects/Tamagoshani/animations/play_left/PlayAnim5.png'),
            scale('C:/Users/angel/PycharmProjects/Tamagoshani/animations/play_left/PlayAnim6.png'),
            scale('C:/Users/angel/PycharmProjects/Tamagoshani/animations/play_right/PlayAnim1.png'),
            scale('C:/Users/angel/PycharmProjects/Tamagoshani/animations/play_right/PlayAnim2.png'),
            scale('C:/Users/angel/PycharmProjects/Tamagoshani/animations/play_right/PlayAnim3.png'),
            scale('C:/Users/angel/PycharmProjects/Tamagoshani/animations/play_right/PlayAnim4.png'),
            scale('C:/Users/angel/PycharmProjects/Tamagoshani/animations/play_right/PlayAnim5.png'),
            scale('C:/Users/angel/PycharmProjects/Tamagoshani/animations/play_right/PlayAnim6.png'),
        ]
    }

    return animations