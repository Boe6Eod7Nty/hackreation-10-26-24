import pygame


# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Ball properties
ball_color = (255, 0, 0)
ball_x = 350
ball_y = 50
ball_radius = 20
ball_speed = 0.5

# Game looppip 
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update ball position
    ball_y += ball_speed

    # Check if ball reached the bottom
    if ball_y + ball_radius > screen_height:
        ball_y = screen_height - ball_radius
        ball_speed = 0

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the ball
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()