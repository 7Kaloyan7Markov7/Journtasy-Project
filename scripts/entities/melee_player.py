from scripts.entities.player import Player
from scripts.enums.enums import Direction, State


class MeleePlayer(Player):
    def attack(self, target=None):
        if target is None:

            # Initiate the swing
            if self.direction == Direction.DOWN or self.direction == Direction.UP:
                return
            if self.weapon.state == State.ATTACKING:
                return
            self.weapon.attack()
            if self.weapon.state == State.ATTACKING:
                self._state = State.ATTACKING
        else:
            # Apply hit to a target
            hit_landed = self.weapon.apply_damage(target, self.stats.damage.damage)
            if hit_landed and target.stats.is_dead:
                self._current_experience += target.exp_on_kill
