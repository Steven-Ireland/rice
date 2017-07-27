from cement.core.controller import CementBaseController, expose
from lib.Stow import Stow
from lib.Git import Git
from lib.Config import Config
import yaml
import os

class SaveCommand(CementBaseController):
    class Meta:
        label = 'install'
        stacked_on = 'base'
        stacked_type = 'embedded'
        arguments = [
            (['extra_arguments'], dict(action='store', nargs='*'))
        ]

    @expose(help='Save a theme', aliases=['i'])
    def save(self):
        ## Note that pretty much everything is a 'happy-path situation right now.
        files = self.app.pargs.extra_arguments[0:-1]
        module = self.app.pargs.extra_arguments[-1]

        currentConfig = Config.load()
        theme = currentConfig['theme'] 
        print('Saving to ' + theme + '/' + module) 

        path = os.path.expanduser('~/.config/rice/' + theme)

        modulePath = path + '/' + module; 
        os.path.makedirs(modulePath);
        
        # Now we need to find the path relative to the home directory
        # If this script is run from .config, and we add .test
        # We need to add .config/test

        cwd = os.cwd()
        homeDir = os.path.expanduser('~')

        # Find the difference between homeDir and cwd

        if (cwd.startswith(homeDir)):
            thing = cwd.split(homeDir)[-1]

        else:
            print("This tool only works for customization under your home directory right now.")


        , path, themeConfig['packages'])

