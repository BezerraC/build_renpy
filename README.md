# Build Project for Ren'Py
This project contains scripts to automate the build process of games developed with Ren'Py for different platforms, including Android and Windows. The scripts are written in Python and use the subprocess library to execute build commands.

## Project Structure
- `build_game.py`: Main script that executes the builds for Android and Windows.
- `build/base_build.py`: Base class that defines the common structure for the builds.
- `build/android_build.py`: Script to build the game for Android.
- `build/windows_build.py`: Script to build the game for Windows.
- `config.py`: Configurations and paths used by the scripts.
- `utils/helpers.py`: Helper functions for checking and creating directories.

## Requirements
- Python 3.x
- JDK 21 in PATH
- Ren'Py SDK (version 8.3.0 or higher)
- Android SDK (for Android build)

## Configuration
Before running the scripts, you must configure the config.py file with the correct paths to the Ren'Py installation, the game directory, and the target directory. Here's an example of how to configure config.py:

```
# config.py

# Path to the installation directory of Ren'Py
RENpy_INSTALLATION_PATH = r"D:\renpy-8.3.0-sdk"

# Directory where the game is located
GAME_DIRECTORY = r"C:\Users\Your\Path\game"

# Directory where builds will be stored
DESTINATION_DIRECTORY = r"C:\Users\Your\Path\dists"
```

## Scripts
`build_game.py`
This script is the main entry point for the build. It creates instances of the `AndroidBuild` and `WindowsBuild` classes and runs the build processes for each platform.

Execution
```
py build_game.py
```
`build/base_build.py`
Defines the BaseBuild base class that contains methods common to all builds, such as run_command.

`build/android_build.py`
Defines the AndroidBuild class, which inherits from BaseBuild and is responsible for building the game for Android.

`build/windows_build.py`
Defines the WindowsBuild class, which inherits from BaseBuild and is responsible for building the game for Windows.

`utils/helpers.py`
Contains helper functions to check and create directories, ensuring that the target directory exists before starting the build.

## How to Run
1. Configure Paths: Make sure the config.py file is correctly configured with the paths to Ren'Py, the game directory, and the target directory.

2. Run Builds: Run the main build_game.py script to start the build process for both platforms (Android and Windows).

```
py build_game.py
```

3. Check Output: After running, check the target directory specified in DESTINATION_DIRECTORY for the generated build files.

## Testing
The project includes unit tests to verify the functionality of the build process. The tests are implemented using Python's unittest framework.

### Test Files
- `tests/test_base_build.py`: Contains tests for the BaseBuild class and its methods.
- `tests/test_android_build.py`: Contains tests for the AndroidBuild class and its methods.
- `tests/test_windows_build.py`: Contains tests for the WindowsBuild class and its methods.
- `tests/test_helpers.py`: Contains tests for helper functions in utils/helpers.py.


### Running Tests
To run the tests, use the following command:
```
py -m unittest discover -s tests
```

## Known Issues
- `Path Errors`: Make sure all paths in config.py are correct and that the specified directories exist.
- `Permissions`: Check the read and write permissions on the specified directories to avoid access errors.

## Author

<img src="https://avatars.githubusercontent.com/u/41126326?v=4" width="150" style="border-radius:15px;" alt="Exemplo imagem">

[@Bezerrac](https://github.com/BezerraC)