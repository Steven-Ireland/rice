from cement.core.controller import CementBaseController, expose
from lib.Stow import Stow
from lib.Git import Git
from lib.Config import Config
import yaml
import os

class InstallCommand(CementBaseController):
    class Meta:
        label = 'install'
        stacked_on = 'base'
        stacked_type = 'embedded'
        arguments = [
            (['extra_arguments'], dict(action='store', nargs='*'))
        ]

    @expose(help='Install a new theme or module', aliases=['i'])
    def install(self):
        arg = self.app.pargs.extra_arguments[0]

        source = arg.split('/')[0]
        theme  = arg.split('/')[1]

        print('Installing ' + arg) 
        path = os.path.expanduser('~/.config/rice/' + theme)

        # If the path exists already, just update
        if (os.path.exists(path)):
            Git.pull(path)
        else:
            Git.clone('https://github.com/' + arg + '.git', path)

        # Load theme configuraiton
        themeConfig = Config.load(path + '/.rice');
        Stow.stow(os.path.expanduser('~'), path, themeConfig['packages'])
