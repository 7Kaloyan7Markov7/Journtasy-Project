from scripts.tiles.tile import Tile


class TileGrid:
    def __init__(self):
        self.tile_list = {}

        for i in range(20):
            for j in range(15):
                position = (i * 40, j * 40)
                tile = Tile(position)

                self.tile_list[position] = tile

                if i - 1 >= 0:
                    tile[((i - 1) * 40, j * 40)].tile_left = tile

                if i + 1 < 20:
                    tile[((i + 1) * 40, j * 40)].tile_right = tile

                if j - 1 >= 0:
                    tile[(i * 40, (j - 1) * 40)].tile_up = tile

                if j + 1 < 15:
                    tile[(i * 40, (j + 1) * 40)].tile_down = tile
                



