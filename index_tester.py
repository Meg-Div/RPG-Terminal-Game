import unittest
import index

class TestActions(unittest.TestCase):
    def test_add_to_hat_dict(self):
        new_hero = index.Hero()

        new_hero.add_to_hat_dict("Cowboy hat", ["rope"])
        hero_hat_dict = new_hero.get_hero_hat_dict()

        self.assertEqual("Cowboy hat" in hero_hat_dict, True)
        self.assertEqual("rope" in hero_hat_dict["Cowboy hat"], True)
        self.assertEqual("flower" in hero_hat_dict["Cowboy hat"], False)

    def test_del_hero_hat_dict(self):
        new_hero = index.Hero()

        new_hero.add_to_hat_dict("Cowboy hat", ["rope"])
        new_hero.del_hero_hat_dict("Cowboy hat")

        self.assertFalse(new_hero.get_hero_hat_dict())

    def test_del_hat_dict(self):
        new_hero = index.Hero()
        new_hero.del_hat_dict("Cowboy hat")

        self.assertTrue("Cowboy hat" not in new_hero.get_hat_dict())

    def test_update_health(self):
        new_hero = index.Hero()

        self.assertTrue(new_hero.get_health(),40)
        new_hero.update_health(-10)
        self.assertTrue(new_hero.get_health(),30)

    def test_del_hero_hat_dict_item(self):
        new_hero = index.Hero()

        new_hero.add_to_hat_dict("Cowboy hat", ["rope", "cow"])
        new_hero.del_hero_hat_dict_item("Cowboy hat", "cow")
        hero_hat_dict = new_hero.get_hero_hat_dict()

        self.assertTrue("cow" not in hero_hat_dict["Cowboy hat"])






if __name__ == '__main__':
    unittest.main()
