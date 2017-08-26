from Job import Job


class Main:

    def __init__(self, task="like"):
        print "Task chosen =", task

        self.task = task
        self.start_job()

    def start_job(self):
        Job(self.task)
