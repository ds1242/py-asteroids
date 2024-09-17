import random
from circleshape import * 
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius < ASTEROID_MIN_RADIUS:
            return
        
        # generate a uniform random angle
        split_angle = random.uniform(20, 50)
        random_angle_positive = self.velocity.rotate(split_angle)
        random_angle_negative = self.velocity.rotate(-split_angle)

        # new radius for the smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # create the asteroids
        asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid_one.velocity = random_angle_positive * 1.2
        asteroid_two.velocity = random_angle_negative