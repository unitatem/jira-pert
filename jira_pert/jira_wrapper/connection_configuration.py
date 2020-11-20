import json


class ConnectionConfiguration(object):
    def __init__(self):
        try:
            self._load_config_file()
        except FileNotFoundError:
            print("W: File not found: server_connection.json")
            self._get_config_data()

    def _load_config_file(self):
        with open('jira_pert/jira_wrapper/server_connection.json') as file:
            data = json.load(file)
            self.server_https = data['server_https']
            self.email = data['email']
            self.api_token = data['api_token']

    def _get_config_data(self):
        self.server_https = input("Server https address:")
        self.email = input("User email address:")
        self.api_token = input("Authentication key:")
