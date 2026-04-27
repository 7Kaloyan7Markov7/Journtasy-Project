from collections import deque

from scripts.tiles.tile import Tile
from scripts.entities.obstacle import Obstacle

class TileGrid:
    def __init__(self):
        self._rows = 15
        self._cols = 20

        self._grid = [[Tile(c * 40, r * 40) for c in range(self._cols)] for r in range(self._rows)]




    def bfs(self, start_pos, end_pos):
        
        return None

    # This method checks if any of the tiles in the grid are colliding with any of the entities
    def set_tile_is_blocking(self, entity_list):
        obstacles = [o for o in entity_list if isinstance(o, Obstacle)]

        for row in self._grid:
            for tile in row:
                for obstacle in obstacles:
                    if tile.hitbox.is_colliding(obstacle.hitbox):
                        tile.is_blocked = True
                
