import pygame

class Star:
    """ Star class """
    def __init__(self, sf_game):
        
        self.settings = sf_game.settings
        self.screen = sf_game.screen
        self.screen_rect = self.screen.get_rect()

        self.star = pygame.image.load('images/star.bmp')
        width = self.star.get_width()
        height = self.star.get_height()

        self.star = pygame.transform.scale(self.star, (width / 10, height / 10))
        self.rect = self.star.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

    def blitme(self):
        self.screen.blit(self.star, self.rect)

    def move(self):
        speed = self.settings.star_speed
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.x += speed
        if self.move_left and self.rect.left > 0:
            self.x -= speed
        if self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += speed
        if self.move_up and self.rect.top > 0:
            self.y -= speed
        
        self.rect.x = self.x
        self.rect.y = self.y

