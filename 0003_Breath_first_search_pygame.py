import pygame
import sys
from maze_generator import Maze

# Constants
WIDTH, HEIGHT, MARGIN = 600, 600, 10
ROWS, COLS = 20, 20  # Update these to match the maze size
CELL_SIZE = WIDTH // COLS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (192, 192, 192)


# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DFS Maze Solver")

maze = Maze(ROWS, COLS, screen, CELL_SIZE, WIDTH, HEIGHT, MARGIN)
start = (0, 0)
goal = (9, 9)


def draw_path(path):
    for (x, y) in path:
        pygame.draw.rect(screen, BLUE, (y * CELL_SIZE + MARGIN, x * CELL_SIZE + MARGIN, CELL_SIZE, CELL_SIZE))
        #pygame.display.update()
        pygame.time.delay(5)

def dfs_maze(maze, start, goal):
    rows, cols = len(maze.grid), len(maze.grid[0])
    queue = [start]
    visited = set()
    path = []

    def is_valid_move(x, y):
        return 0 <= x < rows and 0 <= y < cols and maze.grid[x][y] == 0
    
    while queue:
        x, y = queue.pop(0)
        
        if (x, y) in visited:
            continue
        
        visited.add((x, y))
        path.append((x, y))
        
        screen.fill(BLACK)
        maze.draw_grid()
        draw_path(path)
        pygame.draw.rect(screen, GREEN, (goal[1] * CELL_SIZE + MARGIN, goal[0] * CELL_SIZE + MARGIN, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, RED, (start[1] * CELL_SIZE + MARGIN, start[0] * CELL_SIZE + MARGIN, CELL_SIZE, CELL_SIZE))
        pygame.display.update()
        
        if (x, y) == goal:
            print("Goal found!")
            return True
        
        # Explore neighbors (right, down, left, up)
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if is_valid_move(nx, ny) and (nx, ny) not in visited:
                queue.append((nx, ny))
    
    print("Goal not found.")
    return False

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(BLACK)
    maze.draw_grid()
    pygame.draw.rect(screen, GREEN, (goal[1] * CELL_SIZE + MARGIN, goal[0] * CELL_SIZE + MARGIN, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, RED, (start[1] * CELL_SIZE + MARGIN, start[0] * CELL_SIZE + MARGIN, CELL_SIZE, CELL_SIZE))
    pygame.display.update()
    
    if dfs_maze(maze, start, goal):
        running = False

pygame.quit()
sys.exit()
