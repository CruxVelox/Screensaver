import pygame
import sys
import random
from datetime import datetime

# Initialize Pygame
pygame.init()

# clock font
font_path = "GILSANUB.TTF"
size = 300

# Set up display
fullscreen = True
if fullscreen:
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
else:
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Screensaver")

# Define colors
white = (255, 255, 255)
dark_grey = (28, 28, 28)

# Circle class
class Circle:
    def __init__(self):
        self.radius = random.randint(40, 70)
        self.x = random.randint(self.radius, screen.get_width() - self.radius)
        self.y = random.randint(self.radius, screen.get_height() - self.radius)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.shadow_color = (0, 0, 0)  # Dark color for the shadow
        self.speed_x = random.choice([-1, 1])
        self.speed_y = random.choice([-1, 1])

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Bounce off the walls
        if self.x - self.radius <= 0 or self.x + self.radius >= screen.get_width():
            self.speed_x = -self.speed_x
        if self.y - self.radius <= 0 or self.y + self.radius >= screen.get_height():
            self.speed_y = -self.speed_y

    def draw(self):
        # Draw the shadow
        pygame.draw.circle(screen, self.shadow_color, (self.x + 5, self.y + 5), self.radius)

        # Draw the circle
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

# Create a list of circles
circles = [Circle() for _ in range(500)]

# Font setup
font = pygame.font.Font(font_path, int(size))

# Main loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update
    for circle in circles:
        circle.move()

    # Draw
    screen.fill(dark_grey)
    for circle in circles:
        circle.draw()

    # Get and display the current time with shadow
    current_time = datetime.now().strftime("%H:%M:%S")
    
    # Shadow
    shadow_text = font.render(current_time, True, (50, 50, 50))
    shadow_text_rect = shadow_text.get_rect(center=(screen.get_width() // 2 + 5, screen.get_height() - (screen.get_height() / 2) + 5))
    screen.blit(shadow_text, shadow_text_rect)
    
    # Main text
    text = font.render(current_time, True, white)
    text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() - (screen.get_height() / 2)))
    screen.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(60)  # 60 frames per second
