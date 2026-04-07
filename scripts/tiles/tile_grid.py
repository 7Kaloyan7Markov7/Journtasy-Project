from scripts.tiles.tile import Tile


class TileGrid:
    def __init__(self):
        self.tile_list = {}

        for i in range(20):
            for j in range(15):
                position = (i * 40, j * 40)
                tile = Tile(position)

                self.tile_list[position] = tile

                left_pos = ((i - 1) * 40, j * 40)
                if left_pos in self.tile_list:
                    self.tile_list[left_pos].tile_right = tile
                    tile.tile_left = self.tile_list[left_pos]

                right_pos = ((i + 1) * 40, j * 40)
                if right_pos in self.tile_list:
                    self.tile_list[right_pos].tile_left = tile
                    tile.tile_right = self.tile_list[right_pos]

                up_pos = (i * 40, (j - 1) * 40)
                if up_pos in self.tile_list:
                    self.tile_list[up_pos].tile_down = tile
                    tile.tile_up = self.tile_list[up_pos]

                down_pos = (i * 40, (j + 1) * 40)
                if down_pos in self.tile_list:
                    self.tile_list[down_pos].tile_up = tile
                    tile.tile_down = self.tile_list[down_pos]
                

