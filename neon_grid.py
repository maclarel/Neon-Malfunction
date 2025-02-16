import pygame

class NeonGrid:
    def __init__(self):
        self.elements = []

    def add_element(self, element):
        self.elements.append(element)

    def update(self):
        for element in self.elements:
            element.update()

    def draw(self, screen):
        for element in self.elements:
            element.draw(screen)

    def handle_glitches(self):
        for element in self.elements:
            if isinstance(element, Platform) and element.stability < 50:
                element.stability -= 0.5
                if element.stability <= 0:
                    self.elements.remove(element)
