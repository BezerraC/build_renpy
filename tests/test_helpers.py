import unittest
import os
import shutil
from utils.helpers import verify_or_create_directory
from config import GAME_DIRECTORY

class TestHelpers(unittest.TestCase):
    
    def setUp(self):
        self.test_dir = GAME_DIRECTORY
        if not os.path.exists(self.test_dir):
            os.makedirs(self.test_dir)
    
    def tearDown(self):
        # Clean up the directory before removing it
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
    
    def test_verify_or_create_directory(self):
        # Test directory creation
        verify_or_create_directory(self.test_dir)
        self.assertTrue(os.path.exists(self.test_dir))

if __name__ == '__main__':
    unittest.main()
