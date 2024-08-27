import os

# Path to the directory where the Ren'Py SDK is installed.
# Replace this path with the location where Ren'Py is installed on your machine.
RENpy_INSTALLATION_PATH = r"D:\renpy-8.3.0-sdk"

# Path to the Python executable that comes with the Ren'Py SDK.
# Typically, Python is located inside the Ren'Py SDK's `lib` directory.
# Replace the path if Python is in a different location.
PYTHON_EXECUTABLE = os.path.join(RENpy_INSTALLATION_PATH, "lib", "py3-windows-x86_64", "python.exe")

# Path to the main Ren'Py script. This script is used to run build commands.
# Make sure this path is correct and that the `renpy.py` file is located in this location.
RENpy_SCRIPT = os.path.join(RENpy_INSTALLATION_PATH, "renpy.py")

# Path to the directory where your game is located.
# This directory should contain your Ren'Py project files.
# Replace this path with the directory where your game project is located.
GAME_DIRECTORY = r"D:\renpy-8.3.0-sdk\the_question"

# Path to the directory where the build files will be saved.
# Make sure this directory exists or it will be created by the script if it does not.
# Replace this path with the directory where you want the build files to be stored.
DESTINATION_DIRECTORY = r"C:\Users\Your\Path\dists"
