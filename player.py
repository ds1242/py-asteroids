from circleshape import *
from constants import *


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(PLAYER_RADIUS)
        self.rotation = 0