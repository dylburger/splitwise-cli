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

    def __init__(self, f=CONFIG_FILE):
        YAMLParser.__init__(self, f)
        self.authorize_endpoint = "%s%s" % \
            (self.config['SPLITWISE_SITE'],
             self.config['SPLITWISE_AUTHORIZE_URL'])

        self.request_token_endpoint = "%s%s" % \
            (self.config['SPLITWISE_SITE'],
             self.config['SPLITWISE_REQUEST_TOKEN_URL'])

        self.access_token_endpoint = "%s%s" % \
            (self.config['SPLITWISE_SITE'],
             self.config['SPLITWISE_ACCESS_TOKEN_URL'])

    def __repr__(self):
        return 'SplitwiseConfigParser(AUTH: %s, REQUEST TOKEN: %s, ACCESS TOKEN: %s)' % \
                (self.authorize_endpoint,
                 self.request_token_endpoint,
                 self.access_token_endpoint)

    def get_authorize_endpoint(self):
        """ Retrieves the authorize_endpoint instance variable
        """
        return self.authorize_endpoint

    def get_request_token_endpoint(self):
        """ Retrieves the request_token_endpoint instance variable
        """
        return self.request_token_endpoint

    def get_access_token_endpoint(self):
        """ Retrieves the access_token_endpoint instance variable
        """
        return self.access_token_endpoint


class SplitwiseAPICredentialsParser(YAMLParser):

    def __init__(self, f=CREDENTIALS_FILE):
        YAMLParser.__init__(self, f)
        self.splitwise_api_key = self.config['SPLITWISE_API_KEY']
        self.splitwise_api_secret = self.config['SPLITWISE_API_SECRET']
        self.callback_url = self.config['CALLBACK_URL']

    def __repr__(self):
        """ Just print the API key to identify the Credentials,
            don't print the secret
        """
        return 'SplitwiseAPICredentialsParser(%r)' % (self.splitwise_api_key)

    def get_api_key(self):
        """ Retrieves the splitwise_api_key instance variable
        """
        return self.splitwise_api_key

    def get_api_secret(self):
        """ Retrieves the splitwise_api_secret instance variable
        """
        return self.splitwise_api_secret

    def get_callback_url(self):
        """ Retrieves the callback_url instance variable
        """
        return self.callback_url
