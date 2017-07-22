from subprocess import call
import sys

# Simple python wrapper for GNU Stow
class Stow:
    def stow(installDir, themeDir, packages):
        for package in packages:
            print('- installing package ' + package)
            call(["stow", "-v", "-t", installDir, "-d", themeDir, package], stdout=sys.stdout)
    
