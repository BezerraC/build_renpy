import subprocess

class BaseBuild:
    def __init__(self, python_executable, renpy_script, game_directory, destination_directory, renpy_installation_path):
        self.python_executable = python_executable
        self.renpy_script = renpy_script
        self.game_directory = game_directory
        self.destination_directory = destination_directory
        self.renpy_installation_path = renpy_installation_path 

    def run_command(self, command, cwd):
        try:
            subprocess.run(command, check=True, cwd=cwd)
            print("Build concluída com sucesso!")
        except subprocess.CalledProcessError as e:
            print(f"Ocorreu um erro ao tentar executar o comando: {e}")
