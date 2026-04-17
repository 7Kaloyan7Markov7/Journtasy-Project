import unittest

import scripts.config.constants as const
from scripts.character_stats.health import Health
from scripts.character_stats.damage import Damage
from scripts.character_stats.armor import Armor
from scripts.character_stats.stats import Stats

KNIGHT = const.KNIGHT_ID  # base health=180, growth=22, healing=0.6, armor=14/+3, damage=40/+4


class TestHealth(unittest.TestCase):

    def test_initial_health_level_1(self):
        h = Health(KNIGHT, 1)
        self.assertEqual(h.max_health, 180)
        self.assertEqual(h.current_health, 180)

    def test_initial_health_level_2(self):
        h = Health(KNIGHT, 2)
        self.assertEqual(h.max_health, 202)  # 180 + 22*1
        self.assertEqual(h.current_health, 202)

    def test_take_damage_reduces_health(self):
        h = Health(KNIGHT, 1)
        h.take_damage(50)
        self.assertEqual(h.current_health, 130)

    def test_take_damage_cannot_go_below_zero(self):
        h = Health(KNIGHT, 1)
        h.take_damage(9999)
        self.assertEqual(h.current_health, 0)

    def test_increase_updates_max_health(self):
        h = Health(KNIGHT, 1)
        h.increase(3)
        self.assertEqual(h.max_health, 180 + 22 * 2)  # 224

    def test_healing_does_not_trigger_before_delay(self):
        h = Health(KNIGHT, 1)
        h.take_damage(50)
        for _ in range(29):
            h.update()
        self.assertEqual(h.current_health, 130)

    def test_healing_triggers_after_delay(self):
        h = Health(KNIGHT, 1)
        h.take_damage(50)
        for _ in range(31):
            h.update()
        self.assertAlmostEqual(h.current_health, 130 + 0.6)

    def test_healing_cannot_exceed_max_health(self):
        h = Health(KNIGHT, 1)
        h.take_damage(0.1)
        for _ in range(100):
            h.update()
        self.assertLessEqual(h.current_health, h.max_health)


class TestDamage(unittest.TestCase):

    def test_initial_damage_level_1(self):
        d = Damage(KNIGHT, 1)
        self.assertEqual(d.damage, 40)

    def test_initial_damage_level_3(self):
        d = Damage(KNIGHT, 3)
        self.assertEqual(d.damage, 40 + 4 * 2)  # 48

    def test_increase_updates_damage(self):
        d = Damage(KNIGHT, 1)
        d.increase(2)
        self.assertEqual(d.damage, 44)  # 40 + 4*1


class TestArmor(unittest.TestCase):

    def test_initial_armor_level_1(self):
        a = Armor(KNIGHT, 1)
        self.assertEqual(a.armor, 14)

    def test_initial_armor_level_2(self):
        a = Armor(KNIGHT, 2)
        self.assertEqual(a.armor, 17)  # 14 + 3*1

    def test_reduce_damage_subtracts_armor(self):
        a = Armor(KNIGHT, 1)
        self.assertEqual(a.reduce_damage(30), 16)  # 30 - 14

    def test_reduce_damage_cannot_go_below_zero(self):
        a = Armor(KNIGHT, 1)
        self.assertEqual(a.reduce_damage(5), 0)  # armor(14) > damage(5)

    def test_increase_updates_armor(self):
        a = Armor(KNIGHT, 1)
        a.increase(3)
        self.assertEqual(a.armor, 14 + 3 * 2)  # 20


class TestStats(unittest.TestCase):

    def test_initial_level(self):
        s = Stats(KNIGHT, 1)
        self.assertEqual(s.level, 1)

    def test_is_dead_false_when_alive(self):
        s = Stats(KNIGHT, 1)
        self.assertFalse(s.is_dead)

    def test_is_dead_true_when_health_zero(self):
        s = Stats(KNIGHT, 1)
        s.take_damage(9999)
        self.assertTrue(s.is_dead)

    def test_take_damage_applies_armor_reduction(self):
        s = Stats(KNIGHT, 1)
        s.take_damage(30)
        # armor=14, reduced damage=16, health=180-16=164
        self.assertEqual(s.health.current_health, 164)

    def test_take_damage_blocked_fully_by_armor(self):
        s = Stats(KNIGHT, 1)
        s.take_damage(10)
        self.assertEqual(s.health.current_health, 180)  # armor(14) > damage(10)

    def test_level_up_increments_level(self):
        s = Stats(KNIGHT, 1)
        s.level_up()
        self.assertEqual(s.level, 2)

    def test_level_up_increases_all_stats(self):
        s = Stats(KNIGHT, 1)
        s.level_up()
        self.assertEqual(s.health.max_health, 202)   # 180 + 22
        self.assertEqual(s.armor.armor, 17)           # 14 + 3
        self.assertEqual(s.damage.damage, 44)         # 40 + 4


if __name__ == "__main__":
    unittest.main()
