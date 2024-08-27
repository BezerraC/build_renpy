import unittest
from unittest.mock import patch
from build.android_build import AndroidBuild
from config import PYTHON_EXECUTABLE, RENpy_SCRIPT, GAME_DIRECTORY, DESTINATION_DIRECTORY, RENpy_INSTALLATION_PATH

class TestAndroidBuild(unittest.TestCase):
    
    def setUp(self):
        self.android_builder = AndroidBuild(
            python_executable=PYTHON_EXECUTABLE,
            renpy_script=RENpy_SCRIPT,
            game_directory=GAME_DIRECTORY,
            destination_directory=DESTINATION_DIRECTORY,
            renpy_installation_path=RENpy_INSTALLATION_PATH
        )
    
    @patch('subprocess.run')
    def test_build_android(self, mock_run):
        mock_run.return_value = None
        self.android_builder.build()
        expected_command = [
            PYTHON_EXECUTABLE,
            RENpy_SCRIPT,
            'launcher',
            'android_build',
            GAME_DIRECTORY,
            '--destination', DESTINATION_DIRECTORY
        ]
        mock_run.assert_called_once_with(expected_command, check=True, cwd=RENpy_INSTALLATION_PATH)

if __name__ == '__main__':
    unittest.main()
