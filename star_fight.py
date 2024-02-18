import pygame
import sys
from settings import Settings
from star import Star

class StarFight:
    """ Manage game """
    def __init__(self):
        """ Initialize """

        pygame.init()
        
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        self.star = Star(self)

        pygame.display.set_caption("Star Fight")  
    
    def run_game(self):
        while True:
            self._event_manage()
            self.star.move()
            self._update_screen()
            

    def _event_manage(self):
        """ Menage events """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 sys.exit()
            if event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
                
            if event.type == pygame.KEYUP:
                self._check_keyup_event(event)

    def _check_keydown_event(self,event):
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_RIGHT:
            self.star.move_right = True
        elif event.key == pygame.K_LEFT:
            self.star.move_left = True
        elif event.key == pygame.K_UP:
            self.star.move_up = True
        elif event.key == pygame.K_DOWN:
            self.star.move_down = True

    def _check_keyup_event(self,event):
        if event.key == pygame.K_RIGHT:
            self.star.move_right = False
        elif event.key == pygame.K_LEFT:
            self.star.move_left = False
        elif event.key == pygame.K_UP:
            self.star.move_up = False
        elif event.key == pygame.K_DOWN:
            self.star.move_down = False
                

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.star.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    sf = StarFight()
    sf.run_game()