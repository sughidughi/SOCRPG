import pygame

class BaseScene:
    def __init__(self, scene_manager):
        self.scene_manager = scene_manager
        self.paused = False

    def switch_scene(self, new_scene):
        self.scene_manager.go_to(new_scene)

    def pause(self):
        self.paused = True

    def resume(self):
        self.pasued = False

    def handle_event(self,event):
        pass

    def update(self, delta_time):
        pass

    def draw(self,screen):
        pass