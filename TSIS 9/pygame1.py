import pygame
import colorsys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rainbow Gradient")

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw a circle with rainbow gradient
    radius = 50
    for i in range(radius):
        # Calculate color based on angle
        hue = i / radius  # Hue varies from 0 to 1
        rgb = colorsys.hsv_to_rgb(hue, 1, 1)
        color = tuple(int(c * 255) for c in rgb)  # Convert RGB values to integers
        color_with_alpha = color + (128,)  # Add 50% transparency
        pygame.draw.circle(screen, color_with_alpha, (mouse_x, mouse_y), radius - i, width=5)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
