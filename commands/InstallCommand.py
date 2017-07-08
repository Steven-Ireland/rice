from cement.core.controller import CementBaseController, expose

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
        print(self.app.pargs.extra_arguments) 

