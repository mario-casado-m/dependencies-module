import subprocess, sys

class Dependencies:
    def __init__(self, *args):
        self.packages = list()
        for i in args:
            self.packages.append(i)

    def install_requirements(self):
        for i in self.packages:
            subprocess.call([sys.executable, "-m", "pip", "install", i])