import json


class ConfigProvider:

    def __init__(self):
        self.config_file = "config/task_limits.json"
        self.account_file = "config/account.txt"
        self.comments_file = "config/comments.txt"
        self.hashtags_file = "config/hashtags.txt"

        self.account = self.load_account()
        self.hashtags = self.load_hashtags()
        self.comments = self.load_comments()

        with open(self.config_file) as json_file:
            json_data = json.load(json_file)

            self.task_limits = json_data

    def load_account(self):
        text = open(self.account_file, "r")
        lines = text.read().split(':')
        return {
            'user': lines[0],
            'pass': lines[1]
        }

    def load_hashtags(self):
        text = open(self.hashtags_file, "r")
        return text.read().split('\n')

    def load_comments(self):
        text = open(self.comments_file, "r")
        return text.read().split('\n')

    def get_hashtags(self):
        return self.hashtags

    def get_account(self):
        return self.account

    def get_config_limits(self):
        return self.task_limits
