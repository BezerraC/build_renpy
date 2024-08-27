from build.base_build import BaseBuild

class AndroidBuild(BaseBuild):
    def build(self):
        command = [
            self.python_executable,
            self.renpy_script,
            "launcher",
            "android_build",
            self.game_directory,
            "--destination", self.destination_directory
        ]
        self.run_command(command, self.renpy_installation_path)
