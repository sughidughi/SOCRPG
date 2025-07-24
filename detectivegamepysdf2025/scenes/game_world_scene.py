import pygame
from scenes.base_scene import BaseScene
from scenes.day_cycle_scene import DayCycleScene
from ui.utils import SpriteSheet
class GameWorldScene(BaseScene):
    def __init__(self, scene_manager, overlay_manager):
        super().__init__(scene_manager)
        self.overlay_manager = overlay_manager
        self.spritesheet = SpriteSheet("assets/MC1.png")
        self.frames = [self.spritesheet.get_image(i, 32, 32, scale=2) for i in range(4)]
        self.current_frame = 0
        self.frame_timer = 0
        self.frame_delay = 150  # milliseconds
        self.position = (100, 100)
        self.player = pygame.Rect(400, 300, 32, 32)
        self.terminal = pygame.Rect(600, 300, 32, 32)
        self.font = pygame.font.SysFont(None, 24)
        self.show_interact_prompt = False

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e and self.show_interact_prompt:
                self.overlay_manager.open(DayCycleScene(self.scene_manager))

    def update(self, delta_time):
        keys = pygame.key.get_pressed()
        speed = 200  # pixels per second
        movement = pygame.Vector2(0, 0)
        if keys[pygame.K_w]: movement.y -= 1
        if keys[pygame.K_s]: movement.y += 1
        if keys[pygame.K_a]: movement.x -= 1
        if keys[pygame.K_d]: movement.x += 1
        movement = movement.normalize() if movement.length_squared() > 0 else movement
        self.player.x += movement.x * speed * delta_time
        self.player.y += movement.y * speed * delta_time
        self.player.clamp_ip(pygame.Rect(0, 0, 800, 600))
        # Animation
        self.frame_timer += delta_time * 1000  # convert to milliseconds
        if self.frame_timer >= self.frame_delay:
            self.frame_timer = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)
        # Check interaction
        self.show_interact_prompt = self.player.colliderect(self.terminal)

    def draw(self,screen):
        screen.fill((30, 30, 30))
        
        # Draw terminal and player
        frame = self.frames[self.current_frame]
        screen.blit(frame, self.player.topleft)
        pygame.draw.rect(screen, (200, 100, 255), self.terminal)

        # Prompt
        if self.show_interact_prompt:
            text = self.font.render("Press [E] to access tickets", True, (255, 255, 255))
            screen.blit(text, (self.player.x - 20, self.player.y - 20))
        