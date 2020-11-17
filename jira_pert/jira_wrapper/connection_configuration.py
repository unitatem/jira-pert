import json


class ConnectionConfiguration(object):
    def __init__(self):
        data = self._load_config_file()
        self.server_https = data['server_https']
        self.email = data['email']
        self.api_token = data['api_token']

    @staticmethod
    def _load_config_file():
        with open('jira_pert/jira_wrapper/server_connection.json') as file:
            data = json.load(file)
        return data
