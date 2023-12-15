import pygame
from sys import exit


def show_score():
    get_time = pygame.time.get_ticks()
    score_float = round(get_time / 100 - reset_time, 2)
    score = text_font.render(f'SCORE: {score_float}', False, 'Black')
    score_rect = score.get_rect(topleft=(20, 15))
    screen.blit(score, score_rect)
    return score_float


pygame.init()
screen = pygame.display.set_mode((1000, 499))
pygame.display.set_caption('Khamenei Runner')
clock = pygame.time.Clock()

background = pygame.image.load('img/background.jpg').convert()
background_rest = background.get_rect(topleft=(0, 0))

player_stay = pygame.image.load('img/player-stay.png').convert_alpha()
player_stay_rect = player_stay.get_rect(topleft=(150, 320))

knife = pygame.image.load('img/knife.png').convert_alpha()
knife_rect = knife.get_rect(midtop=(1000, 325))

text_font = pygame.font.Font('font/NineTsukiRegular.ttf', 50)

game_over_text = text_font.render('TRY ONE MORE TIME', False, 'Black')
game_over_text_rect = game_over_text.get_rect(center=(480, 120))

player_dead = pygame.image.load('img/dead_player.png').convert_alpha()
player_dead_rect = player_dead.get_rect(center=(460, 230))

player_gravity = 0
game_active = 1
reset_time = 0
SCORE = 0
high_score = 0

userevent = pygame.USEREVENT + 1
pygame.time.set_timer(userevent, 1500)

while True:
    print(a)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == userevent:
            print('1')

    if game_active:
        screen.blit(background, background_rest)
        screen.blit(knife, knife_rect)
        screen.blit(player_stay, player_stay_rect)
        SCORE = show_score()

        background_rest.right -= 5
        knife_rect.right -= 5

        if knife_rect.right <= 0:
            knife_rect.right = 1000
        if background_rest.right <= 1000:
            background_rest.right = 3000
        player_gravity += 1
        player_stay_rect.y += player_gravity

        if player_stay_rect.y > 320:
            player_stay_rect.y = 320

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and player_stay_rect.y >= 300:
            player_gravity = -20

        # if player_stay_rect.colliderect(knife_rect):
        #     game_active = 0
    else:
        screen.fill('yellow')

        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            game_active = 1
            knife_rect.x = 1000
        if SCORE > high_score:
            high_score = SCORE

        reset_time = pygame.time.get_ticks() / 100

        death_score = text_font.render(f'SCORE: {SCORE}', True, 'Black')
        death_score_rect = death_score.get_rect(center=(480, 350))

        high_score_text = text_font.render(f'HIGH SCORE: {high_score}', True, 'Black')
        high_score_text_rect = high_score_text.get_rect(center=(480, 400))
        screen.blit(player_dead, player_dead_rect)
        screen.blit(game_over_text, game_over_text_rect)
        screen.blit(death_score, death_score_rect)
        screen.blit(high_score_text, high_score_text_rect)

    pygame.display.update()
    clock.tick(60)
