import pygame

class TicketCard:
    WIDTH = 600
    HEIGHT = 100
    PADDING = 10

    PRIORITY_COLORS = {
        "LOW": (100, 200, 100),      # Green
        "MEDIUM": (255, 215, 0),     # Yellow
        "HIGH": (255, 100, 100),     # Red
        "CRITICAL": (150, 0, 0),     # Darker Red (optional for later)
    }

    def __init__(self, priority, title, position):
        self.priority = priority
        self.title = title
        self.position = position
        self.rect = pygame.Rect(position[0], position[1], self.WIDTH, self.HEIGHT)
        self.font = pygame.font.SysFont("arial", 20)
        self.title_surface = self.font.render(title, True, (255, 255, 255))
        self.priority_surface = self.font.render(f"Priority: {priority}", True, (50, 50, 50))

    def draw(self, screen):
        # Card background color based on priority
        color = self.PRIORITY_COLORS.get(self.priority.upper(), (200, 200, 200))
        pygame.draw.rect(screen, color, self.rect, border_radius=8)

        # Card border
        pygame.draw.rect(screen, (20, 20, 20), self.rect, width=2, border_radius=8)

        # Draw text
        screen.blit(self.title_surface, (self.position[0] + self.PADDING, self.position[1] + self.PADDING))
        screen.blit(self.priority_surface, (self.position[0] + self.PADDING, self.position[1] + 40))
