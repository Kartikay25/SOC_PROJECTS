import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, RED, BLUE
from player   import Player
from game     import Game
from renderer import draw_grid, draw_players
 
 
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock  = pygame.time.Clock()
 
    player1 = Player(start_row=40, start_col=20, start_direction=(0,  1), color=RED,  player_id=1)
    player2 = Player(start_row=40, start_col=60, start_direction=(0, -1), color=BLUE, player_id=2)
    game = Game(rows=80, cols=80)
    game.add_player(player1)
    game.add_player(player2)
 
    
    player_colors = {
        1: RED,
        2: BLUE,
    }

    running = True
    while running:
        clock.tick(FPS)
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
 
            elif event.type == pygame.KEYDOWN:
 
                if event.key == pygame.K_UP and player1.direction != (1, 0):
                    player1.direction = (-1, 0)
                elif event.key == pygame.K_DOWN and player1.direction != (-1, 0):
                    player1.direction = (1, 0)
                elif event.key == pygame.K_LEFT and player1.direction != (0, 1):
                    player1.direction = (0, -1)
                elif event.key == pygame.K_RIGHT and player1.direction != (0, -1):
                    player1.direction = (0, 1)
 
                elif event.key == pygame.K_w and player2.direction != (1, 0):
                    player2.direction = (-1, 0)
                elif event.key == pygame.K_s and player2.direction != (-1, 0):
                    player2.direction = (1, 0)
                elif event.key == pygame.K_a and player2.direction != (0, 1):
                    player2.direction = (0, -1)
                elif event.key == pygame.K_d and player2.direction != (0, -1):
                    player2.direction = (0, 1)
 
              
                elif event.key == pygame.K_r:
                    game.reset()
 
 
        game.update()
 
        screen.fill((0, 0, 0))
        draw_grid(screen, game, player_colors)
        draw_players(screen, game)
        pygame.display.update()
 
    pygame.quit()
 
 
if __name__ == "__main__":
    main()
