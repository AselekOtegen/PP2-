import pygame


# Function to interpolate between two colors
def interpolate_color(color1, color2, alpha):
    return (
        int(color1[0] * (1 - alpha) + color2[0] * alpha),
        int(color1[1] * (1 - alpha) + color2[1] * alpha),
        int(color1[2] * (1 - alpha) + color2[2] * alpha)
    )

# Function to draw the gradient
def draw_gradient(surface, direction):
    width, height = surface.get_size()
    colors = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (75, 0, 130), (238, 130, 238)]  # Rainbow colors

    if direction == 'horizontal':
        for x in range(width):
            color_index = int((x / width) * (len(colors) - 1))
            color1 = colors[color_index]
            color2 = colors[color_index + 1]
            for y in range(height):
                alpha = y / height
                color = interpolate_color(color1, color2, alpha)
                surface.set_at((x, y), color)
    elif direction == 'vertical':
        for y in range(height):
            color_index = int((y / height) * (len(colors) - 1))
            color1 = colors[color_index]
            color2 = colors[color_index + 1]
            for x in range(width):
                alpha = x / width
                color = interpolate_color(color1, color2, alpha)
                surface.set_at((x, y), color)

# Main function
def main():
    pygame.init()
    size = (800, 600)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Custom Gradient")

    direction = 'horizontal'  # Change to 'vertical' for vertical gradient
    font = pygame.font.SysFont(None, 24)  # Font for displaying RGB values

    draw_gradient(screen, direction)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = 'horizontal'
                    draw_gradient(screen, direction)
                elif event.key == pygame.K_RIGHT:
                    direction = 'vertical'
                    draw_gradient(screen, direction)

        # Get RGB values at mouse position
        x, y = pygame.mouse.get_pos()
        rgb_value = screen.get_at((x, y))

        # Clear previous RGB text
        screen.fill((0, 0, 0), (0, 0, 200, 50))

        # Render and blit new RGB text
        text = font.render(f"RGB: {rgb_value[0]}, {rgb_value[1]}, {rgb_value[2]}", True, (255, 255, 255))
        screen.blit(text, (10, 10))

        pygame.display.flip()

if __name__ == "__main__":
    main()
