class OverlayManager:
    def __init__(self):
        self.overlays = []

    def open(self, overlay):
        self.overlays.append(overlay)

    def close(self, overlay=None):
        if overlay:
            if overlay in self.overlays:
                self.overlays.remove(overlay)

        else:
            # Close all overlays
            self.overlays.clear()

    def handle_event(self, event):
            if self.overlays:
                 self.overlays[-1].handle_event(event)

    def update(self, delta_time):
         if self.overlays:
              self.overlays[-1].update(delta_time)

    def draw(self,screen):
         for overlay in self.overlays:
              overlay.draw(screen)

    def is_overlay_active(self):
         return bool(self.overlays)