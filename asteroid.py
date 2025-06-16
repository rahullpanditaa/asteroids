import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", (self.position), self.radius, 2)

    def update(self, dt):
        forward = pygame.Vector2(0, 1).rotate(0)
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        angle = random.uniform(20, 50)

        # new_vector_one = pygame.Vector2(0, 1).rotate(angle)
        new_vector_one = self.velocity.rotate(angle)
        new_vector_two = self.velocity.rotate(-angle)
        # new_vector_two = pygame.Vector2(0, 1).rotate(-angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_one.velocity = new_vector_one * 1.2

        asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_two.velocity = new_vector_two * 1.2