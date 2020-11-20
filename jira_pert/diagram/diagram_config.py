import json


class DiagramConfig(object):
    def __init__(self):
        self.config = dict()
        self._load_config_file()

    def _load_config_file(self):
        with open('jira_pert/diagram/diagram_config.json') as file:
            self.config = json.load(file)
