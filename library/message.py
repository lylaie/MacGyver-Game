import pygame.font

class Message():
    
    def __init__(self, window, msg): 

        self.window = window
        self.window_rect = window.get_rect()

        self.width, self.height = 250, 100
        self.message_color = (230, 230, 230)
        self.text_message_color = (0,0,0)
        self.font_message = pygame.font.SysFont(None,48)

        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.center = self.window_rect.center

        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font_message.render(msg, True, self.text_message_color, self.message_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_message(self):
        self.window.fill(self.message_color, self.rect)
        self.window.blit(self.msg_image, self.msg_image_rect)
