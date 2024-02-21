import pygame
from settings import *


class Button:
    def __init__(self, x, y, width, height, text='', color=(73, 73, 73), text_color=(255, 255, 255), font_size=13, border_radius = R_BUTTON, action = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.text_color = text_color
        self.border_radius = border_radius
        self.font_size = font_size
        self.action = action

    def __str__(self) -> str:
        return self.text

    def get_action(self):
        if self.action is None:
            return self.text
        else:
            return self.action 

    """
    Draws the button
    :param screen: the screen where the button is going to be drawn
    :param x_pos: the horizontal position of the button
    :type x_pos: Int
    :param y_pos: the vertical position of the button
    :type y_pos: int
    :param mouse_pos: the position of the mouse
    :type mouse_pos: Tuple[Int,Int]
    :return: None
    """

    def draw(self, screen, x_pos: int, y_pos: int, mouse_pos: tuple[int, int]) -> None:
        if not x_pos is None:
            self.x = x_pos
            self.y = y_pos

        # invert colors if mouse is over the button
        button_color = self.text_color if self.is_over(mouse_pos) else self.color
        text_color = self.color if self.is_over(mouse_pos) else self.text_color

        # Draw the button rectangle
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, button_color, rect, border_radius=self.border_radius)

        # Draw the text on the button
        if self.text != '':
            try:
                font = pygame.font.Font(FONT_PATH, self.font_size)
            except Exception as e:
                print(f"Error loading font: {e}")
                font = pygame.font.SysFont('Arial', self.font_size)

            text_surface = font.render(self.text, True, text_color)
            screen.blit(text_surface, (self.x + (self.width - text_surface.get_width()) / 2,
                                       self.y + (self.height - text_surface.get_height()) / 2))

    """
    Checks if the mouse is over the button
    :param mouse_pos: the position of the mouse
    :type mouse_pos: Tuple[Int,Int]
    :return: True if the mouse is over the button, false otherwise
    :rtype: Bool
    """

    def is_over(self, mouse_pos: tuple[int, int]) -> bool:
        if self.x is None: return False

        # Pos is the mouse position as a tuple (x, y)
        if self.x < mouse_pos[0] < self.x + self.width and \
                self.y < mouse_pos[1] < self.y + self.height:
            return True
        return False
