import pygame

class Items():
    
    def __init__(self, window, number_items):
        self.number_items = number_items
        self.bg_color = (230, 230, 230)
        self.window = window
        self.window_rect = self.window.get_rect()
        self.text_color = (60, 60, 60)
        self.font = pygame.font.SysFont(None, 40)
        self.prep_items(self.number_items)

    def prep_items(self, number_items):
        item_str = str(self.number_items)
        self.items_image = self.font.render(item_str, True, self.text_color, self.bg_color)
        self.items_image_rect = self.items_image.get_rect()
        self.items_image_rect.right = self.window_rect.right - 15
        self.items_image_rect.top = 10

    def show_number_items(self):
        self.window.blit(self.items_image, self.items_image_rect)
