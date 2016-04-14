import unittest
import pet
import pet.models


class TestPetModels(unittest.TestCase):

    def setUp(self):
        pass

    def test_get_col_spec(self):
        debversion = pet.models.DebVersion()
        self.assertEqual("DEBVERSION", debversion.get_col_spec())

    def test_bind_processor(self):
        debversion = pet.models.DebVersion()
        process = debversion.bind_processor(None)
        value = 123
        self.assertEqual(process(value), value)

    def test_result_processor(self):
        debversion = pet.models.DebVersion()
        process = debversion.result_processor(None, None)
        value = 123
        self.assertEqual(process(value), value)

    def test_vcs_if_vcs_exists(self):
        repository = pet.models.Repository()
        value = 123
        repository._vcs = value
        self.assertEqual(repository.vcs, value)
