import pygame
import random
screen_width = 640
screen_height = 480
# Configurações globais
square_size = 80  # Tamanho do quadrado na grid
num_initial_collectibles = 5  # Número inicial de colecionáveis
min_collectibles = 5  # Número mínimo de colecionáveis

# Lista de posições dos colecionáveis
collectible_positions = []

# Tempo inicial
start_time = pygame.time.get_ticks()


def add_collectibles(num_collectibles, collectible_image):
    for _ in range(num_collectibles):
        collectible_x = random.randint(0, screen_width - collectible_image.get_width())
        collectible_y = random.randint(0, screen_height - collectible_image.get_height())
        collectible_positions.append((collectible_x, collectible_y))

def update_collectibles(screen_width, screen_height, collectible_image, player1, player2):
    """Atualiza a lista de colecionáveis e verifica colisões."""
    global collectible_positions
    # Adiciona novos colecionáveis se necessário
    if len(collectible_positions) < min_collectibles:
        add_collectibles(2)

    # Verifica colisões com os colecionáveis
    for position in collectible_positions[:]:
        if player1.rect.colliderect(
                pygame.Rect(position[0], position[1], collectible_image.get_width(), collectible_image.get_height())):
            player1.score += 1
            collectible_positions.remove(position)

        if player2.rect.colliderect(
                pygame.Rect(position[0], position[1], collectible_image.get_width(), collectible_image.get_height())):
            player2.score += 1
            collectible_positions.remove(position)


def draw(screen, background, collectible_image, player1, player2):
    """Desenha todos os elementos gráficos do jogo na tela."""
    screen.blit(background, (0, 0))

    # Desenha as grades
    for x in range(0, screen.get_width(), square_size):
        pygame.draw.line(screen, (0, 0, 0), (x, 0), (x, screen.get_height()))
    for y in range(0, screen.get_height(), square_size):
        pygame.draw.line(screen, (0, 0, 0), (0, y), (screen.get_width(), y))

    # Desenha os colecionáveis
    for position in collectible_positions:
        screen.blit(collectible_image, position)

    # Desenha os jogadores
    screen.blit(player1.image, player1.rect)
    screen.blit(player2.image, player2.rect)

    # Desenha as pontuações dos jogadores
    font = pygame.font.Font(None, 36)
    score_text_player1 = font.render(f'Player 1 Score: {player1.score}', True, (0, 0, 0))
    score_text_player2 = font.render(f'Player 2 Score: {player2.score}', True, (0, 0, 0))
    screen.blit(score_text_player1, (10, 10))
    screen.blit(score_text_player2, (10, 50))

    # Desenha o tempo decorrido
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
    timer_text = font.render(f'{elapsed_time} s', True, (0, 0, 0))
    screen.blit(timer_text, (screen.get_width() - timer_text.get_width() - 10, 10))


def check_end_game():
    """Verifica se o jogo deve terminar com base no tempo decorrido."""
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
    return elapsed_time >= 30  # Encerra após 30 segundos


def determine_winner(player1, player2):
    """Determina o vencedor do jogo com base nas pontuações."""
    if player1.score > player2.score:
        return "Player 1"
    elif player2.score > player1.score:
        return "Player 2"
    else:
        return "Tie"


def display_winner(screen, winner, screen_width, screen_height):
    """Mostra o vencedor na tela após o fim do jogo."""
    font_winner = pygame.font.Font(None, 50)
    winner_text = font_winner.render(f'Congratulations: {winner}', True, (0, 0, 0))
    screen.blit(winner_text, (screen_width // 2 - 150, screen_height // 2 - 25))


def game_loop(screen, background, collectible_image, player1, player2):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True  # End game

        player1.handle_event(event)
        player2.handle_event(event)

    update_collectibles(screen.get_width(), screen.get_height(), collectible_image, player1, player2)
    draw(screen, background, collectible_image, player1, player2)
    pygame.display.flip()

    return check_end_game()
