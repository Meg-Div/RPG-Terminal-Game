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

if __name__ == '__main__':
    unittest.main()
