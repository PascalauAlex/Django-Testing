import unittest


from app import SuperHero

class TestSuperHero(unittest.TestCase):
    def setUp(self):
        self.superhero = SuperHero(name="Superman", strength_level=50)

    def test_stringify(self):
        self.assertEqual(str(self.superhero), "Superman")

    def test_is_stronger_than_other_superhero(self):
        other_superhero = SuperHero(name="Batman",strength_level=35)
        self.assertTrue(self.superhero.is_stronger_than(other_superhero))
        self.assertFalse(other_superhero.is_stronger_than(self.superhero))
