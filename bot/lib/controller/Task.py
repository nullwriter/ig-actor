import datetime
import random
import time
from LikeTask import LikeTask
from GetCommentTask import GetCommentTask


class Task:

    def __init__(self, taskname, hashtags, limits, api):
        self.task_name = taskname
        self.hashtags = hashtags
        self.limits = limits
        self.task_count = 0
        self.api = api
        self.task = ""

    def start_task(self):
        print ""
        print "#################################################"
        print "  Starting new Job Task at {:%d-%m-%Y %H:%M:%S}".format(datetime.datetime.now())
        print "#################################################"
        print ""

        if self.task_name == "like":
            self.task = LikeTask(self)
        if self.task_name == "extract-comment":
            self.task = GetCommentTask(self)

        self.task.init_task()

    def check_ops_limit(self):

        sleep_time = self.limits[self.task_name]['wait_restart']
        minutes = sleep_time / 60

        if self.task_count >= self.limits[self.task_name]['max_ops']:
            print ""
            print "Max operations reached, will sleep for " + str(minutes) + " minutes."
            print ""
            time.sleep(sleep_time)

        return True

    def get_time_delay(self):
        return random.randint(int(self.limits[self.task_name]['delay_from']), int(self.limits[self.task_name]['delay_to']))
