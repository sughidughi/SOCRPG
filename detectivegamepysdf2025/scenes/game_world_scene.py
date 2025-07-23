import pygame
from scenes.day_cycle_scene import DayCycleScene
from ui.utils import SpriteSheet
class GameWorldScene:
    def __init__(self, scene_manager, overlay_manager):
        self.scene_manager = scene_manager
        self.overlay_manager = overlay_manager
        self.spritesheet = SpriteSheet("assets/MC1.png")
        self.frames = [
            self.spritesheet.get_image(i, 32, 32, scale=2)
            for i in range(4)
        ]
        self.current_frame = 0
        self.frame_timer = 0
        self.frame_delay = 150
        self.position = (100, 100)
        self.player = pygame.Rect(400, 300, 32, 32)
        self.terminal = pygame.Rect(600, 300, 32, 32)
        self.font = pygame.font.SysFont(None, 24)
        self.show_interact_prompt = False

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e and self.show_interact_prompt:
                self.overlay_manager.open(DayCycleScene(self.scene_manager))

    def update(self):
        keys = pygame.key.get_pressed()
        speed = 4
        if keys[pygame.K_w]:
            self.player.y -= speed
        if keys[pygame.K_s]:
            self.player.y += speed
        if keys[pygame.K_a]:
            self.player.x -= speed
        if keys[pygame.K_d]:
            self.player.x += speed
        self.player.clamp_ip(pygame.Rect(0, 0, 800, 600))
        # Animation
        self.frame_timer += 1
        if self.frame_timer >= self.frame_delay // 10:
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
        