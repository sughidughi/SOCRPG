# main.py
import pygame
from scene_manager import SceneManager
from ui.overlay_manager import OverlayManager
from scenes.day_cycle_scene import DayCycleScene

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("SOC Forensics RPG")
clock = pygame.time.Clock()

# Initialize scene manager
overlay_manager = OverlayManager()
scene_manager = SceneManager(overlay_manager)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            overlay_manager.close() # Close top or all overlays
        
        if overlay_manager.is_overlay_active():
            overlay_manager.handle_event(event)
        else:
            scene_manager.handle_event(event)

    if overlay_manager.is_overlay_active():
        overlay_manager.update()
    else:
        scene_manager.update()

    scene_manager.draw(screen)
    if overlay_manager.is_overlay_active():
        overlay_manager.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
