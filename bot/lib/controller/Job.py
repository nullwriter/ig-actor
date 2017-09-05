from Task import Task


class Job:

    def __init__(self, task):
        from ..model.ConfigProvider import ConfigProvider
        self.config = ConfigProvider()
        self.task = task

        account = self.config.get_account()

        from ..InstagramAPI import InstagramAPI
        self.api = InstagramAPI(account['user'], account['pass'])
        self.hashtags = self.config.get_hashtags()
        self.limits = self.config.get_config_limits()

        self.task_obj = Task(self.task, self.hashtags, self.limits, self.api)

        if self.login():
            self.task_obj.start_task()
        else:
            print "Could not login to IG. Please try again."

    def login(self):
        return self.api.login()
