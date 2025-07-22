# scenes/day_cycle_scene.py

import pygame
from ui.ticket_card import TicketCard

class DayCycleScene:
    def __init__(self, scene_manager):
        self.scene_manager = scene_manager
        self.tickets = self.generate_tickets()
        self.selected_ticket = None
        self.font = pygame.font.SysFont("arial", 24)

    def generate_tickets(self):
        return [
            TicketCard("LOW", "Workstation can't connect to Wi-Fi", (50, 100 )),
            TicketCard("MEDIUM", "Phishing email reported by user", (50, 220)),
            TicketCard("HIGH", "Suspicious outbound traffic from server", (50, 340)),
        ]
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            for ticket in self.tickets:
                if ticket.rect.collidepoint(mouse_pos):
                    self.selected_ticket = ticket
                    print (f"Selected ticket: {ticket.title}")
    
    def update(self):
        # Placeholder (logic like animations or time-based events go here eventually)
        pass

    def draw(self, screen):
        screen.fill((30, 30, 30)) # Dark background for SOC environment

        title_surface = self.font.render("Day Cycle: Handle SOC Tickets", True, (255, 255, 255))
        screen.blit(title_surface, (50, 30))

        for ticket in self.tickets:
            ticket.draw(screen)

        # Optional (highlight selected ticket)
        if self.selected_ticket:
            pygame.draw.rect(screen, (255, 255, 0), self.selected_ticket.rect, 3)