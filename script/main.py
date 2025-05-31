import pygame
import random

pygame.init()
clock = pygame.time.Clock()

info = pygame.display.Info()
screen_width = info.current_w
screen_height = info.current_h

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Shanezhka')
icon = pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/images/icon.png')
pygame.display.set_icon(icon)

background = pygame.image.load('C:/Users/angel/PycharmProjects/Tamagoshani/images/background.png')
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
    ]
}

animation_scale_percentage = 20 / 100  # 20%

current_state = 'idle'
player_anim_count = 0
background_x = 0

animation_speed = 500
last_frame_time = pygame.time.get_ticks()

player_x = (screen_width - 100) // 2
player_y = (screen_height - 100) // 2
move_speed = 5


def change_state():
    global current_state
    states = ['idle', 'walk_right', 'walk_left']
    current_state = random.choice(states)


running = True
while running:
    current_time = pygame.time.get_ticks()

    screen.blit(background, (background_x, 0))
    screen.blit(background, (background_x + screen_width, 0))

    current_animation = animations[current_state]
    current_frame = current_animation[player_anim_count]

    original_width, original_height = current_frame.get_size()

    max_width = int(screen_width * animation_scale_percentage)
    max_height = int(screen_height * animation_scale_percentage)

    scale_factor = min(max_width / original_width, max_height / original_height)
    new_width = int(original_width * scale_factor)
    new_height = int(original_height * scale_factor)

    current_frame = pygame.transform.scale(current_frame, (new_width, new_height))

    center_x = player_x
    center_y = player_y

    screen.blit(current_frame, (center_x, center_y))

    if current_state == 'walk_right':
        player_x += move_speed

    if current_state == 'walk_left':
        player_x -= move_speed

    if current_time - last_frame_time > animation_speed:
        player_anim_count = (player_anim_count + 1) % len(current_animation)
        last_frame_time = current_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if random.randint(1, 100) < 5:
        change_state()

    pygame.display.update()

    clock.tick(60)

pygame.quit()
