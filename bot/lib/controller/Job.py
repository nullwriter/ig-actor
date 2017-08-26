import datetime
import random
import time



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
        self.task_count = 0
        self.start_task()

    def like_task(self):

        hash_index = 0
        loop = True
        max_index = len(self.hashtags)
        next_max_id = ""

        while loop:

            self.check_ops_limit()

            current_hash = self.hashtags[hash_index]
            self.api.getHashtagFeed(current_hash, maxid=next_max_id)

            print ""
            print "CURRENT HASHTAG = "+current_hash
            print ""
            
            ig_media = self.api.LastJson

            if "next_max_id" not in ig_media:
                print "####### Changing hashtag #######"
                hash_index += 1
                next_max_id = ""
                if hash_index >= max_index-1:
                    break
            else:
                next_max_id = self.do_likes(ig_media)

        print "Finished doing likes for all hashes. Count =", self.task_count

    def do_likes(self, ig_media):
        last_max_id = ig_media['next_max_id']

        if "ranked_items" in ig_media:
            key = "ranked_items"
        else:
            key = "items"

        for ig in ig_media[key]:

            if self.api.like(ig["pk"]):
                print "*** [" + str(self.task_count) + "] Liked a picture!"
                self.task_count += 1
            else:
                print "--- Could not send like... trying again"
            time.sleep(self.get_time_delay())

        return last_max_id

    def check_ops_limit(self):

        sleep_time = self.limits[self.task]['wait_restart']
        minutes = sleep_time / 60

        if self.task_count >= self.limits[self.task]['max_ops']:
            print ""
            print "Max operations reached, will sleep for "+str(minutes)+" minutes."
            print ""
            time.sleep(sleep_time)

        return True

    def get_time_delay(self):
        return random.randint(int(self.limits[self.task]['delay_from']), int(self.limits[self.task]['delay_to']))

    def start_task(self):
        print ""
        print "#################################################"
        print "  Starting new Job Task at {:%d-%m-%Y %H:%M:%S}".format(datetime.datetime.now())
        print "#################################################"
        print ""

        self.login()

        if self.task == "like":
            self.like_task()

    def login(self):
        return self.api.login()
