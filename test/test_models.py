import unittest
import pet.models
import pet
from sqlalchemy.exc import OperationalError
import os.path
from mock import MagicMock


class TestPetModels(unittest.TestCase):

    def setUp(self):
        pass

    def test_check_ssl_certificate_with_file(self):
        os.path.isfile = MagicMock(return_value=True)
        pet.engine = MagicMock(return_value=True)
        engine = pet.models.check_ssl_certificate()
        self.assertIsNotNone(engine)

    def test_check_ssl_certificate_with_file_ex(self):
        os.path.isfile = MagicMock(return_value=True)
        pet.engine = MagicMock(side_effect=OperationalError("", {}, None))
        engine = pet.models.check_ssl_certificate()
        self.assertIsNone(engine)

    def test_check_ssl_certificate_no_file(self):
        os.path.isfile = MagicMock(return_value=False)
        pet.engine = MagicMock(return_value=True)
        engine = pet.models.check_ssl_certificate()
        self.assertIsNotNone(engine)

    def test_check_ssl_certificate_no_file_ex(self):
        os.path.isfile = MagicMock(return_value=False)
        pet.engine = MagicMock(side_effect=OperationalError("", {}, None))
        engine = pet.models.check_ssl_certificate()
        self.assertIsNone(engine)
