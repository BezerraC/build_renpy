from config import PYTHON_EXECUTABLE, RENpy_SCRIPT, GAME_DIRECTORY, DESTINATION_DIRECTORY, RENpy_INSTALLATION_PATH
from utils.helpers import verify_or_create_directory
from build.android_build import AndroidBuild
from build.windows_build import WindowsBuild

# Check if directories exist
verify_or_create_directory(GAME_DIRECTORY)
verify_or_create_directory(DESTINATION_DIRECTORY)

if __name__ == "__main__":
    print("Iniciando o build para Android...")
    android_builder = AndroidBuild(PYTHON_EXECUTABLE, RENpy_SCRIPT, GAME_DIRECTORY, DESTINATION_DIRECTORY, RENpy_INSTALLATION_PATH)
    android_builder.build()

    print("Iniciando o build para Windows...")
    windows_builder = WindowsBuild(PYTHON_EXECUTABLE, RENpy_SCRIPT, GAME_DIRECTORY, DESTINATION_DIRECTORY, RENpy_INSTALLATION_PATH)
    windows_builder.build()

    print("Builds concluídos com sucesso!")

    
