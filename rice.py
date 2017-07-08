#!/usr/bin/env python

from cement.core.foundation import CementApp
from cement.core.controller import CementBaseController, expose

from commands.InstallCommand import InstallCommand

class RiceClient(CementBaseController):
    class Meta:
        label = 'base'
        description = 'Some rice thing to make it sound like I had a cool name' 

class RiceApp(CementApp):
    class Meta:
        label = 'rice'
        base_controller = 'base'
        handlers = [RiceClient, InstallCommand]

with RiceApp() as app:
    app.run()
