import pygame
from constants import ROWS, COLS, CELL_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, GRAY, WHITE
 
 
def draw_grid(screen, game, player_colors):
    
    for row in range(ROWS):
        for col in range(COLS):
            cell_value = game.grid[row, col]
 
            if cell_value == 0:
                color = BLACK
            else:
                color = player_colors.get(cell_value, BLACK)
 
            pixel_x = col * CELL_SIZE
            pixel_y = row * CELL_SIZE
            pygame.draw.rect(screen, color, (pixel_x, pixel_y, CELL_SIZE, CELL_SIZE))
 
    for x in range(0, SCREEN_WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (SCREEN_WIDTH, y))
 
 
def draw_players(screen, game):
    for player in game.players:
        if not player.alive:
            continue
 
        center_x = player.col * CELL_SIZE + CELL_SIZE // 2
        center_y = player.row * CELL_SIZE + CELL_SIZE // 2
        radius   = CELL_SIZE // 2 - 1
 
        pygame.draw.circle(screen, WHITE, (center_x, center_y), radius)
