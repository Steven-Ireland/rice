from subprocess import call
import sys
import yaml
import os

# Glorified yaml reader
class Config:
    def load(path=os.path.expanduser('~/.config/rice/.ricecfg')):
        return yaml.load(open(path), 'rw');
        
