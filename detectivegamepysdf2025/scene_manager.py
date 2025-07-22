# scene_manager.py
from scenes.game_world_scene import GameWorldScene

class SceneManager:
    def __init__(self, overlay_manager):
        self.overlay_manager = overlay_manager
        self.current_scene = GameWorldScene(self, overlay_manager) # Start in game world

    def handle_event(self, event):
            self.current_scene.handle_event(event)
    
    def update(self):
        self.current_scene.update()

    def draw(self, screen):
        self.current_scene.draw(screen)