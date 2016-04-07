import unittest
import pet

class TestPetInit(unittest.TestCase):

    def setUp(self):
        pass

    def test_engine(self):
        engine = pet.engine()
        self.assertIsNotNone(engine)
