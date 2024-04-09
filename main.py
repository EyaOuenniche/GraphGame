import pygame
import sys
import networkx as nx
import matplotlib.pyplot as plt

# Initialize pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tracking Covid-19 Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 150, 150)  # Pastel red
GREEN = (150, 255, 150)  # Pastel green
BLUE = (150, 150, 255)  # Pastel blue

# Define fonts
font = pygame.font.SysFont(None, 60)

# Function to display the start screen
def display_start_screen():
    # Load background image
    background_image = pygame.image.load("backgroundimage.jpg").convert()
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    
    screen.blit(background_image, (0, 0))
    
    title_text = font.render("Game to track COVID-19 spread", True, BLACK)
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3))
    screen.blit(title_text, title_rect)
    start_text = font.render("Play", True, BLACK)
    start_rect = start_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    pygame.draw.rect(screen, RED, start_rect, border_radius=5)
    pygame.draw.rect(screen, BLACK, start_rect, 2, border_radius=5)
    screen.blit(start_text, start_rect)
    pygame.display.flip()

# Function to display the level selection screen
def display_level_selection_screen():
    # Load background image
    levelscreen_image = pygame.image.load("levelscreen.jpg").convert()
    levelscreen_image = pygame.transform.scale(levelscreen_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Blit background image
    screen.blit(levelscreen_image, (0, 0))
    
    # Draw title
    title_text = font.render("Choose Your Level", True, BLACK)
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 6))
    screen.blit(title_text, title_rect)
    
    # Draw level buttons
    button_width, button_height = 200, 50
    button_gap = 20
    total_button_height = (button_height + button_gap) * 4
    start_y = (SCREEN_HEIGHT - total_button_height) // 2
    for i in range(4):
        button_rect = pygame.Rect((SCREEN_WIDTH - button_width) // 2, start_y + i * (button_height + button_gap), button_width, button_height)
        pygame.draw.rect(screen, GREEN, button_rect, border_radius=5)
        pygame.draw.rect(screen, BLACK, button_rect, 2, border_radius=5)
        level_text = font.render(f"Level {i+1}", True, BLACK)
        level_rect = level_text.get_rect(center=button_rect.center)
        screen.blit(level_text, level_rect)

    # Add back button
    back_text = font.render("<-", True, BLACK)
    back_rect = back_text.get_rect(center=(SCREEN_WIDTH // 10, SCREEN_HEIGHT // 10))
    pygame.draw.rect(screen, BLUE, back_rect, border_radius=5)
    pygame.draw.rect(screen, BLACK, back_rect, 2, border_radius=5)
    screen.blit(back_text, back_rect)
    pygame.display.flip()

# Function to display the level screen
import networkx as nx

def display_level_screen(level):
    screen.fill(WHITE)
    level_text = font.render(f"Level {level}", True, BLACK)
    level_rect = level_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(level_text, level_rect)
    
    # Add back button
    back_text = font.render("<-", True, BLACK)
    back_rect = back_text.get_rect(center=(SCREEN_WIDTH // 10, SCREEN_HEIGHT // 10))
    pygame.draw.rect(screen, GREEN, back_rect, border_radius=5)
    pygame.draw.rect(screen, BLACK, back_rect, 2, border_radius=5)
    screen.blit(back_text, back_rect)
    
    # Create a complete graph with 5 vertices
    G = nx.complete_graph(5)
    pos = nx.spring_layout(G, seed=42)  # Positions of nodes
    labels = {0: "sam", 1: "john", 2: "lilian", 3: "adams", 4: "ahmad"}
    nx.draw(G, pos, with_labels=True, labels=labels, node_color=BLUE, node_size=500, font_size=12, font_color=BLACK, edge_color=BLACK)
    
    pygame.display.flip()


# Main loop
current_screen = "start"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if current_screen == "start":
                current_screen = "level_selection"
            elif current_screen == "level_selection":
                # Check if any level button is clicked
                button_width, button_height = 200, 50
                button_gap = 20
                start_y = (SCREEN_HEIGHT - ((button_height + button_gap) * 4)) // 2
                for i in range(4):
                    button_rect = pygame.Rect((SCREEN_WIDTH - button_width) // 2, start_y + i * (button_height + button_gap), button_width, button_height)
                    if button_rect.collidepoint(event.pos):
                        current_screen = f"level_{i+1}"
                        break
                # Check if back button is clicked
                back_rect = pygame.Rect(SCREEN_WIDTH // 10 - 25, SCREEN_HEIGHT // 10 - 25, 50, 50)
                if back_rect.collidepoint(event.pos):
                    current_screen = "start"
            elif current_screen.startswith("level_"):
                # Check if back button is clicked
                back_rect = pygame.Rect(SCREEN_WIDTH // 10 - 25, SCREEN_HEIGHT // 10 - 25, 50, 50)
                if back_rect.collidepoint(event.pos):
                    current_screen = "level_selection"
    if current_screen == "start":
        display_start_screen()
    elif current_screen == "level_selection":
        display_level_selection_screen()
    elif current_screen.startswith("level_"):
        level = int(current_screen.split("_")[1])
        display_level_screen(level)







