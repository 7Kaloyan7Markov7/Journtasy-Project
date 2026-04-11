from scripts.tiles.tile import Tile
from scripts.entities.obstacle import Obstacle
from scripts.enums.enums import Direction


class TileGrid:
    def __init__(self):
        self.tile_list = {}

        for i in range(20):
            for j in range(15):
                position = (i * 40, j * 40)
                self.tile_list[position] = Tile(position)

        for i in range(20):
            for j in range(15):
                position = (i * 40, j * 40)
                tile = self.tile_list[position]

                neighbors = {
                    Direction.LEFT:  ((i - 1) * 40, j * 40),
                    Direction.RIGHT: ((i + 1) * 40, j * 40),
                    Direction.UP:    (i * 40, (j - 1) * 40),
                    Direction.DOWN:  (i * 40, (j + 1) * 40),
                }

                for direction, pos in neighbors.items():
                    if pos in self.tile_list:
                        tile.adjacent_tiles[direction] = self.tile_list[pos]

    def set_tile_is_blocking(self, entity_list):
        for _, tile in self.tile_list.items():
            for entity in entity_list:
                if isinstance(entity, Obstacle) and entity.hitbox.is_colliding(tile.hitbox):
                    tile.is_blocked = True
