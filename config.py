""" Classes and methods to handle config variables
    used in Splitwise project
"""

from __future__ import print_function
import yaml

CONFIG_FILE = "config.yml"
CREDENTIALS_FILE = ".oauth_credentials"


class YAMLParser():
    """ Small class to read in and retrieve the data
        found in YAML files, handling basic exceptions
    """
    def __init__(self, FILE):
        with open(FILE, 'r') as f:
            try:
                config = yaml.load(f)
            except yaml.YAMLError as exc:
                print("Your config file appears to contain invalid YAML: ",
                      exc)
            else:
                self.config = config


class SplitwiseConfigParser(YAMLParser):

    def __init__(self):
        YAMLParser.__init__(self, CONFIG_FILE)

    def __repr__(self):
        return 'SplitwiseConfigParser(%r)' % (self.config)


class SplitwiseAPICredentialsParser(YAMLParser):

    def __init__(self):
        YAMLParser.__init__(self, CREDENTIALS_FILE)

    def __repr__(self):
        return 'SplitwiseAPICredentialsParser(%r)' % (self.config)
