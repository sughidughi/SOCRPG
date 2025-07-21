import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Detective Mystery RPG")

# Define colors
BLUE = (0, 255, 204)
YELLOW = (255, 215, 0)
GRAY = (160, 160, 160)
DARK_PURPLE = (26, 26, 46)
DARK_RED = (46, 26, 26)

# Clock
clock = pygame.time.Clock()
speed = 4

# Base Scene class
class Scene:
    def handle_input(self):
        pass

    def render(self):
        pass

# Main Room Scene
class MainRoom(Scene):
    def __init__(self, screen, switch_scene):
        self.screen = screen
        self.switch_scene = switch_scene
        self.player = pygame.Rect(100, 300, 40, 40)
        self.door = pygame.Rect(750, 300, 40, 80)

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.x -= speed
        if keys[pygame.K_RIGHT]:
            self.player.x += speed
        if keys[pygame.K_UP]:
            self.player.y -= speed
        if keys[pygame.K_DOWN]:
            self.player.y += speed

        # Prevents player from leaving screen
        self.player.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))

        # Scene Transition
        if self.player.colliderect(self.door):
            self.switch_scene("crime_scene")
            self.player.x, self.player.y = 100, 100

    def render(self):
        self.screen.fill(DARK_PURPLE)
        pygame.draw.rect(self.screen, BLUE, self.player)
        pygame.draw.rect(self.screen, GRAY, self.door)
        pygame.display.flip()

# Crime Scene
class CrimeScene(Scene):
    def __init__(self, screen, switch_scene):
        self.screen = screen
        self.switch_scene = switch_scene
        self.player = pygame.Rect(100, 100, 40, 40)

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.x -= speed
        if keys[pygame.K_RIGHT]:
            self.player.x += speed
        if keys[pygame.K_UP]:
            self.player.y -= speed
        if keys[pygame.K_DOWN]:
            self.player.y += speed
        # Prevent player from leaving screen
        self.player.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))

        # Scene transition
        if self.player.x < 10:
            self.switch_scene("main")
            self.player.x, self.player.y = 100, 300

    def render(self):
        self.screen.fill(DARK_RED)
        pygame.draw.rect(self.screen, (255, 153, 153), self.player)
        pygame.display.flip()

# Pause/Menu Scene
class MenuScene:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 36)
        self.options = ["Inventory", "Save", "Exit"]
        self.selected = 0

    def draw(self):
        self.screen.fill((30, 30, 60))
        title = self.font.render("Options", True, (255, 255, 255))
        self.screen.blit(title, (250, 100))

        for idx, option in enumerate(self.options):
            color = (200, 200, 255) if idx == self.selected else (150, 150, 150)
            text = self.font.render(option, True, color)
            self.screen.blit(text, (300, 200 + idx * 60))

    def run(self):
        running = True
        clock = pygame.time.Clock()
        while running:
            self.draw()
            pygame.display.flip()
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return  # Resume game
                    elif event.key == pygame.K_UP:
                        self.selected = (self.selected - 1) % len(self.options)
                    elif event.key == pygame.K_DOWN:
                        self.selected = (self.selected + 1) % len(self.options)
                    elif event.key == pygame.K_RETURN:
                        if self.options[self.selected] == "Inventory":
                            print("🧳 Inventory selected (placeholder)")
                        elif self.options[self.selected] == "Save":
                            print("💾 Game saved (placeholder)")
                        elif self.options[self.selected] == "Exit":
                            pygame.quit()
                            sys.exit()

# Scene Manager
class SceneManager:
    def __init__(self, screen):
        self.screen = screen
        self.scenes = {
            "main": MainRoom(screen, self.switch_scene),
            "crime_scene": CrimeScene(screen, self.switch_scene)
        }
        self.current_scene_name = "main"
        self.current_scene = self.scenes[self.current_scene_name]

    def switch_scene(self, name):
        self.current_scene_name = name
        self.current_scene = self.scenes[name]

    def run(self):
        while True:
            # Input and update
            self.current_scene.handle_input()

            # Global escape key check
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    menu = MenuScene(self.screen)
                    menu.run()

            # Render current scene
            self.current_scene.render()
            clock.tick(60)

# Run the game
manager = SceneManager(win)
manager.run()
