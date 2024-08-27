import unittest
from unittest.mock import patch
from build.windows_build import WindowsBuild
from config import PYTHON_EXECUTABLE, RENpy_SCRIPT, GAME_DIRECTORY, DESTINATION_DIRECTORY, RENpy_INSTALLATION_PATH

class TestWindowsBuild(unittest.TestCase):
    
    def setUp(self):
        self.windows_builder = WindowsBuild(
            python_executable=PYTHON_EXECUTABLE,
            renpy_script=RENpy_SCRIPT,
            game_directory=GAME_DIRECTORY,
            destination_directory=DESTINATION_DIRECTORY,
            renpy_installation_path=RENpy_INSTALLATION_PATH
        )
    
    @patch('subprocess.run')
    def test_build_windows(self, mock_run):
        mock_run.return_value = None
        self.windows_builder.build()
        expected_command = [
            PYTHON_EXECUTABLE,
            RENpy_SCRIPT,
            'launcher',
            'distribute',
            GAME_DIRECTORY,
            '--format', 'zip',
            '--package', 'win',
            '--destination', DESTINATION_DIRECTORY
        ]
        mock_run.assert_called_once_with(expected_command, check=True, cwd=RENpy_INSTALLATION_PATH)

if __name__ == '__main__':
    unittest.main()
