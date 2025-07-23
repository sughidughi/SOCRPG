import pygame

class SpriteSheet:
    def __init__(self, filename):
        self.sheet = pygame.image.load("assets/MC1.png").convert_alpha()

    def get_image(self, frame, width, height, scale=1):
        image = pygame.Surface((width,height), pygame.SRCALPHA)
        image.blit(self.sheet, (0,0), (frame * width, 0, width, height))
        if scale!= 1:
            image = pygame.transform.scale(image, (int(width * scale), int(height*scale)))
            return image