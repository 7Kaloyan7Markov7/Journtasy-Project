class CollisionManager:
    def manage_all_collisions(self, room):
        self.manage_player_enemy_collisions(room)
        self.manage_weapon_enemy_collisions(room)
        self.manage_player_obstacle_collisions(room)
        self.manage_enemy_obstacle_collisions(room)

    def manage_player_enemy_collisions(self, room):
        ...

    def manage_weapon_enemy_collisions(self, room):
        ...

    def manage_player_obstacle_collisions(self, room):
        ...

    def manage_enemy_obstacle_collisions(self, room):
        ...

    def obstacle_colliding_obstacle(self, room):
        ...