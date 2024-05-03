import pygame
import server.server_impl.gamemechs as gamemechs
from client import Player1, Player2

pygame.init()

# Screen settings
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Python/Survival on the Edge")

# Load images
background = pygame.image.load('client/ui/assets/ice.png').convert()
collectible_image = pygame.image.load('client/ui/assets/bag.png').convert_alpha()


# Clock for frame rate control
clock = pygame.time.Clock()
# Variável para contar o tempo decorrido
start_time = pygame.time.get_ticks()

# Lista de posições para os recursos
collectible_positions = []

# Create players
player1 = Player1((150, 150))
player2 = Player2((300, 300))
# Pontuação inicial dos jogadores
score_player1 = 0
score_player2 = 0
# Define as configurações da grade
grid_width = 20  # Largura de cada célula da grade
grid_height = 20  # Altura de cada célula da grade
rows = screen_height // grid_height  # Número de linhas na grade
cols = screen_width // grid_width  # Número de colunas na grade

# Função para desenhar a grade na tela
def draw_grid():
    for x in range(0, screen_width, grid_width):
        pygame.draw.line(screen, (200, 200, 200), (x, 0), (x, screen_height))
    for y in range(0, screen_height, grid_height):
        pygame.draw.line(screen, (200, 200, 200), (0, y), (screen_width, y))

# Desenha a grade
draw_grid()

# Game loop
game_over = False
square_size = 40

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        # Passa os eventos para ambos os jogadores
        player1.handle_event(event)
        player2.handle_event(event)

    # Atualiza os jogadores
    player1.update(player1.direction)
    player2.update(player2.direction)
    # Desenha o background
    screen.blit(background, (0, 0))

    # Desenha a grid
    for x in range(0, screen_width, square_size):
        pygame.draw.line(screen, (200, 200, 200), (x, 0), (x, screen_height))
    for y in range(0, screen_height, square_size):
        pygame.draw.line(screen, (200, 200, 200), (0, y), (screen_width, y))
    # Verifica limites das bordas
    #player1.rect.clamp_ip(screen.get_rect())
    #player2.rect.clamp_ip(screen.get_rect())

    # Verifica colisão com as malas
    for position in collectible_positions[:]:
        if player1.rect.collidepoint(position):
            score_player1 += 1
            collectible_positions.remove(position)

        if player2.rect.collidepoint(position):
            score_player2 += 1
            collectible_positions.remove(position)

    # Calcula o tempo decorrido
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000

    # Desenha o background
    screen.blit(background, (0, 0))

    # Desenha a borda
    #screen.blit(border_image, (0, 0))

    # Desenha as malas
    for position in collectible_positions:
        screen.blit(collectible_image, position)

    # Desenha os jogadores
    screen.blit(player1.image, player1.rect)
    screen.blit(player2.image, player2.rect)

    # Desenha os identificadores dos jogadores
    font = pygame.font.Font(None, 24)
    player1_id = font.render("1", True, (0, 0, 0))  # Cor branca
    player2_id = font.render("2", True, (0, 0, 0))  # Cor branca
    screen.blit(player1_id, (player1.rect.x + player1.rect.width // 2 - 10, player1.rect.y - 20))
    screen.blit(player2_id, (player2.rect.x + player2.rect.width // 2 - 10, player2.rect.y - 20))

    # Desenha a pontuação dos jogadores na tela
    font_score = pygame.font.Font(None, 36)
    score_text_player1 = font_score.render(f'Jogador 1 Pontuação: {score_player1}', True, (0, 0, 0))  # Cor preta
    score_text_player2 = font_score.render(f'Jogador 2 Pontuação: {score_player2}', True, (0, 0, 0))  # Cor preta
    # Determina a posição inicial do texto
    text_position_x = 10
    text_position_y = 10

    # Desenha um retângulo por trás do texto da pontuação do jogador 1
    pygame.draw.rect(screen, (255, 255, 255), (
    text_position_x, text_position_y, score_text_player1.get_width(), score_text_player1.get_height()))
    screen.blit(score_text_player1, (text_position_x, text_position_y))

    # Atualiza a posição X para o texto do jogador 2
    text_position_x += score_text_player1.get_width() + 10

    # Desenha um retângulo por trás do texto da pontuação do jogador 2
    pygame.draw.rect(screen, (255, 255, 255), (
    text_position_x, text_position_y, score_text_player2.get_width(), score_text_player2.get_height()))
    screen.blit(score_text_player2, (text_position_x, text_position_y))
    # Desenha o tempo decorrido na tela com um retângulo sólido por trás no canto inferior direito
    timer_text = font_score.render(f'Tempo: {elapsed_time} s', True, (0, 0, 0))  # Cor preta

    # Determina a posição do texto do timer no canto inferior direito
    timer_text_width, timer_text_height = timer_text.get_size()
    timer_text_x = screen_width - timer_text_width - 10
    timer_text_y = screen_height - timer_text_height - 10

    # Desenha um retângulo por trás do texto do timer
    pygame.draw.rect(screen, (255, 255, 255),
                     (timer_text_x - 5, timer_text_y - 5, timer_text_width + 10, timer_text_height + 10))
    screen.blit(timer_text, (timer_text_x, timer_text_y))
    # Desenha um retângulo por trás do texto do timer
    pygame.draw.rect(screen, (255, 255, 255),
                     (timer_text_x, timer_text_y, timer_text.get_width(), timer_text.get_height()))
    screen.blit(timer_text, (timer_text_x, timer_text_y))

    # Adiciona novas malas à medida que algumas são coletadas
    if len(collectible_positions) < 5:
        gamemechs.add_collectibles(2,collectible_image)

    # Verifica se o tempo limite foi atingido
    if elapsed_time >= 30:
        game_over = True

    pygame.display.flip()
    clock.tick(15)

# Determina o vencedor
winner = "None"
if score_player1 > score_player2:
    winner = "Jogador 1"
elif score_player2 > score_player1:
    winner = "Jogador 2"
else:
    winner = "Empate"

# Exibe o vencedor na tela
font_winner = pygame.font.Font(None, 50)
winner_text = font_winner.render(f'Parabéns: {winner}', True, (0, 0, 0))  # Cor vermelha
screen.blit(winner_text, (screen_width // 2 - 100, screen_height // 2 - 25))
pygame.display.flip()

# Aguarda um momento antes de encerrar
pygame.time.delay(3000)

pygame.quit()
