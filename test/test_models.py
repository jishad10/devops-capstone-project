"""
Test cases for Account Model
"""
import os
import logging
import unittest
from service import app
from service.models import Account, DataValidationError, db
from tests.factories import AccountFactory

DATABASE_URI = os.getenv(
    "DATABASE_URI", "postgresql+psycopg2://postgres:postgres@localhost:5432/postgres"
)


class TestAccountModel(unittest.TestCase):
    """Test Cases for Account Model"""

    @classmethod
    def setUpClass(cls):
        """Run once before all tests"""
        app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
        app.config["TESTING"] = True
        app.logger.setLevel(logging.CRITICAL)
        app.app_context().push()

    @classmethod
    def tearDownClass(cls):
        """Run once after all tests"""
        db.session.close()

    def setUp(self):
        """Run before each test"""
        db.session.query(Account).delete()
        db.session.commit()

    def tearDown(self):
        db.session.remove()

    ######################################################################
    #  T E S T   C A S E S
    ######################################################################

    def test_create_an_account(self):
        """It should Create an Account and assert that it exists"""
        account = AccountFactory()
        account.create()
        self.assertIsNotNone(account.id)
        found = Account.all()
        self.assertEqual(len(found), 1)

    def test_read_account(self):
        """It should Read an Account"""
        account = AccountFactory()
        account.create()

        found_account = Account.find(account.id)
        self.assertEqual(found_account.id, account.id)
        self.assertEqual(found_account.name, account.name)
        self.assertEqual(found_account.email, account.email)

    def test_serialize_an_account(self):
        """It should Serialize an account"""
        account = AccountFactory()
        serial_account = account.serialize()
        self.assertEqual(serial_account["id"], account.id)
        self.assertEqual(serial_account["name"], account.name)
        self.assertEqual(serial_account["email"], account.email)

    def test_deserialize_an_account(self):
        """It should Deserialize an account"""
        account = AccountFactory()
        serial_account = account.serialize()
        new_account = Account()
        new_account.deserialize(serial_account)
        self.assertEqual(new_account.name, account.name)
        self.assertEqual(new_account.email, account.email)