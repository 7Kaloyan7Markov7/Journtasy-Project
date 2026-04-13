from collections import deque

from scripts.tiles.tile import Tile
from scripts.entities.obstacle import Obstacle
from scripts.enums.enums import Direction


class TileGrid:
    def __init__(self):
        self.tile_list = {}

        opposites = {
            Direction.LEFT: Direction.RIGHT,
            Direction.RIGHT: Direction.LEFT,
            Direction.UP: Direction.DOWN,
            Direction.DOWN: Direction.UP,
        }

        for i in range(20):
            for j in range(15):
                position = (i * 40, j * 40)
                tile = Tile(position)
                self.tile_list[position] = tile

                #potentially add adjacent tiles to the tile's adjacent_tiles dictionary
                neighbors = {
                    Direction.LEFT:  ((i - 1) * 40, j * 40),
                    Direction.RIGHT: ((i + 1) * 40, j * 40),
                    Direction.UP:    (i * 40, (j - 1) * 40),
                    Direction.DOWN:  (i * 40, (j + 1) * 40),
                }

                for direction, pos in neighbors.items():
                    if pos in self.tile_list:
                        tile.adjacent_tiles[direction] = self.tile_list[pos]
                        self.tile_list[pos].adjacent_tiles[opposites[direction]] = tile

    def bfs(self, start_pos, end_pos):
        if start_pos not in self.tile_list or end_pos not in self.tile_list:
            return None

        start = self.tile_list[start_pos]
        end = self.tile_list[end_pos]

        queue = deque([(start, [start])])
        visited = {start}

        while queue:
            current, path = queue.popleft()
            if current is end:
                return path
            for neighbor in current.adjacent_tiles.values():
                if neighbor is not None and neighbor not in visited and not neighbor.is_blocked:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))

        return None

    # This method checks if any of the tiles in the grid are colliding with any of the entities
    def set_tile_is_blocking(self, entity_list):
        for _, tile in self.tile_list.items():
            for entity in entity_list:
                if isinstance(entity, Obstacle) and entity.hitbox.is_colliding(tile.hitbox):
                    tile.is_blocked = True
