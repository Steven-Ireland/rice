from subprocess import call
import sys

# Simple python wrapper for Git
class Git:
    def pull(themeDir):
        call(["git", "--git-dir", themeDir + '/.git', "pull"], stdout=sys.stdout)

    def clone(fromUrl, themeDir):
        call(["git", "clone", fromUrl, themeDir], stdout=sys.stdout)
