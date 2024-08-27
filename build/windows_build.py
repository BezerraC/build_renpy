from build.base_build import BaseBuild

class WindowsBuild(BaseBuild):
    def build(self):
        command = [
            self.python_executable,
            self.renpy_script,
            "launcher",
            "distribute",
            self.game_directory,
            "--format", "zip",
            "--package", "win",
            "--destination", self.destination_directory
        ]
        self.run_command(command, self.renpy_installation_path)
