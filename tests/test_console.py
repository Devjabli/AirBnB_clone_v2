import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User

class TestHBNBCommand(unittest.TestCase):
    """Test the HBNBCommand console class."""

    def setUp(self):
        """Set up the test environment."""
        storage.reset()  # Make sure to reset storage before each test
        self.console = HBNBCommand()

    def test_create(self):
        """Test the create command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('create User name="John" age=30')
            user_id = f.getvalue().strip()
            self.assertTrue(user_id in storage.all().keys())

    def test_show(self):
        """Test the show command."""
        user = User(name="John", age=30)
        user.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'show User {user.id}')
            output = f.getvalue().strip()
            self.assertIn(user.id, output)

    def test_destroy(self):
        """Test the destroy command."""
        user = User(name="John", age=30)
        user.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'destroy User {user.id}')
            self.assertNotIn(user.id, storage.all().keys())

    def test_all(self):
        """Test the all command."""
        user1 = User(name="John", age=30)
        user2 = User(name="Jane", age=25)
        user1.save()
        user2.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('all User')
            output = f.getvalue().strip()
            self.assertIn(user1.id, output)
            self.assertIn(user2.id, output)

    def test_update(self):
        """Test the update command."""
        user = User(name="John", age=30)
        user.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'update User {user.id} name "Doe"')
            self.console.onecmd(f'show User {user.id}')
            output = f.getvalue().strip()
            self.assertIn("Doe", output)

    def test_count(self):
        """Test the count command."""
        user1 = User(name="John", age=30)
        user2 = User(name="Jane", age=25)
        user1.save()
        user2.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('User.count()')
            output = f.getvalue().strip()
            self.assertEqual(output, '2')

    def tearDown(self):
        """Clean up after each test."""
        storage.reset()  # Make sure to reset storage after each test

if __name__ == '__main__':
    unittest.main()
