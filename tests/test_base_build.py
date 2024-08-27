import unittest
from unittest.mock import patch
from build.base_build import BaseBuild
from config import PYTHON_EXECUTABLE, RENpy_SCRIPT, GAME_DIRECTORY, DESTINATION_DIRECTORY, RENpy_INSTALLATION_PATH

class TestBaseBuild(unittest.TestCase):
    
    def setUp(self):
        self.build = BaseBuild(
            python_executable=PYTHON_EXECUTABLE,
            renpy_script=RENpy_SCRIPT,
            game_directory=GAME_DIRECTORY,
            destination_directory=DESTINATION_DIRECTORY,
            renpy_installation_path=RENpy_INSTALLATION_PATH
        )
    
    @patch('subprocess.run')
    def test_run_command_success(self, mock_run):
        mock_run.return_value = None
        command = ['echo', 'hello']
        self.build.run_command(command, cwd='.')
        mock_run.assert_called_once_with(command, check=True, cwd='.')

if __name__ == '__main__':
    unittest.main()
