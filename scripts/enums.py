from enum import Enum, auto


class Direction(Enum):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3
    NO_DIRECTION = 4

class State(Enum):
    IDLE = 0
    MOVING = 1
    ATTACKING = 2
    DEAD = 3
    NO_STATE = 4