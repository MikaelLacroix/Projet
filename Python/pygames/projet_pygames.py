import pygame
import random
import sys
import json

# commencer le jeu
pygame.init()

# Constante
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
FPS = 60

# Creer l'écran
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Click Rapide")

# horloge pour controler le temps de jeu
clock = pygame.time.Clock()

# Fonts
font = pygame.font.Font(None, 36)

# Game variables
score = 0

# Load highscores depuis un file json
def load_highscores():
    try:
        with open('highscores.json', 'r') as f:
            data = f.read()
            if data:
                highscores = json.loads(data)
            else:
                highscores = []
    except FileNotFoundError:
        highscores = []
    return highscores


# Save highscores file json
def save_highscores(highscores):
    with open('highscores.json', 'w') as f:
        json.dump(highscores, f)

highscores = load_highscores()

def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game()
                elif event.key == pygame.K_2:
                    show_highscores()
                elif event.key == pygame.K_3:
                    pygame.quit()
                    sys.exit()

        screen.fill(WHITE)
        menu_text = font.render("Menu:", True, (0, 0, 0))
        screen.blit(menu_text, (10, 10))
        option1_text = font.render("1. Nouvelle Partie", True, (0, 0, 0))
        screen.blit(option1_text, (10, 50))
        option2_text = font.render("2. Voir les scores", True, (0, 0, 0))
        screen.blit(option2_text, (10, 90))
        option3_text = font.render("3. Quitter", True, (0, 0, 0))
        screen.blit(option3_text, (10, 130))

        pygame.display.flip()
        clock.tick(FPS)

def show_highscores():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        screen.fill(WHITE)
        font = pygame.font.Font(None, 36)
        title_text = font.render("Highscores", True, (0, 0, 0))
        screen.blit(title_text, (10, 10))

        # Trier les highscores en ordre décroissant
        sorted_highscores = sorted(highscores, key=lambda x: x[1], reverse=True)

        # Afficher les highscores triés
        font = pygame.font.Font(None, 24)
        y = 50
        for idx, (name, score) in enumerate(sorted_highscores):
            score_text = font.render(f"{idx + 1}. {name}: {score}", True, (0, 0, 0))
            screen.blit(score_text, (10, y))
            y += 30

        pygame.display.flip()
        clock.tick(FPS)


def game():
    global score
    score = 0
    game_time = 20
    game_over = False

    blue_rect = pygame.Rect(random.randint(0, SCREEN_WIDTH - 20), random.randint(0, SCREEN_HEIGHT - 20), 20, 20)
    red_rect = pygame.Rect(random.randint(0, SCREEN_WIDTH - 20), random.randint(0, SCREEN_HEIGHT - 20), 20, 20)
    ball_pos = [random.randint(0, SCREEN_WIDTH - 40), random.randint(0, SCREEN_HEIGHT - 40)]
    ball_speed = [2, 2]

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # clique gauche
                    if blue_rect.collidepoint(event.pos):
                        score += 10
                        blue_rect = pygame.Rect(random.randint(0, SCREEN_WIDTH - 20), random.randint(0, SCREEN_HEIGHT - 20), 20, 20)
                    elif red_rect.collidepoint(event.pos):
                        score -= 5
                        red_rect = pygame.Rect(random.randint(0, SCREEN_WIDTH - 20), random.randint(0, SCREEN_HEIGHT - 20), 20, 20)
                elif event.button == 3:  # clique droit
                    if blue_rect.collidepoint(event.pos):
                        score -= 5
                        blue_rect = pygame.Rect(random.randint(0, SCREEN_WIDTH - 20), random.randint(0, SCREEN_HEIGHT - 20), 20, 20)
                    elif red_rect.collidepoint(event.pos):
                        score += 10
                        red_rect = pygame.Rect(random.randint(0, SCREEN_WIDTH - 20), random.randint(0, SCREEN_HEIGHT - 20), 20, 20)
                if blue_rect.collidepoint(event.pos):
                    blue_rect = pygame.Rect(random.randint(0, SCREEN_WIDTH - 20), random.randint(0, SCREEN_HEIGHT - 20), 20, 20)
                if red_rect.collidepoint(event.pos):
                    red_rect = pygame.Rect(random.randint(0, SCREEN_WIDTH - 20), random.randint(0, SCREEN_HEIGHT - 20), 20, 20)

        # déplacer la balle
        ball_pos[0] += ball_speed[0]
        ball_pos[1] += ball_speed[1]

        # collision avec les murs
        if ball_pos[0] < 0 or ball_pos[0] > SCREEN_WIDTH - 10:
            ball_speed[0] = -ball_speed[0]
        if ball_pos[1] < 0 or ball_pos[1] > SCREEN_HEIGHT - 10:
            ball_speed[1] = -ball_speed[1]

        game_time -= 1 / FPS
        if game_time <= 0:
            game_over = True

        screen.fill(WHITE)
        pygame.draw.rect(screen, BLUE, blue_rect)
        pygame.draw.rect(screen, RED, red_rect)
        pygame.draw.circle(screen, (255, 0, 0), ball_pos, 10)
        score_text = font.render(f"Score: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))
        time_text = font.render(f"Time: {int(game_time)}", True, (0, 0, 0))
        screen.blit(time_text, (SCREEN_WIDTH - 150, 10))

        pygame.display.flip()
        clock.tick(FPS)

    game_over_screen()


def game_over_screen():
    input_box = pygame.Rect(100, 200, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        # ajouter le score du joueur dans la liste des highscores
                        highscores.append((text, score))
                        save_highscores(highscores)  # enregister dans le fichier highscores
                        done = True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

                if event.key == pygame.K_ESCAPE:
                    done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive

        screen.fill(WHITE)
        
        # Afficher le texte "Entrez votre nom :"
        font = pygame.font.Font(None, 36)
        text_surface = font.render("Entrez votre nom :", True, (0, 0, 0))
        screen.blit(text_surface, (100, 150))
        
        # Afficher la zone de texte
        pygame.draw.rect(screen, color, input_box)
        font = pygame.font.Font(None, 32)
        txt_surface = font.render(text, True, (0, 0, 0))
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.display.flip()

    show_highscores()


# loop du jeu
while True:
    main_menu()





