import time


class LikeTask:

    def __init__(self, task, name="like"):
        self.name = name
        self.task = task

    def init_task(self):

        hash_index = 0
        loop = True
        max_index = len(self.task.hashtags)
        next_max_id = ""

        while loop:

            self.task.check_ops_limit()

            current_hash = self.task.hashtags[hash_index]
            self.task.api.getHashtagFeed(current_hash, maxid=next_max_id)

            print ""
            print "CURRENT HASHTAG = " + current_hash
            print ""

            ig_media = self.task.api.LastJson

            if "next_max_id" not in ig_media:
                print "####### Changing hashtag #######"
                hash_index += 1
                next_max_id = ""
                if hash_index >= max_index - 1:
                    break
            else:
                next_max_id = self.do_task(ig_media)

        print "Finished doing likes for all hashes. Count =", self.task.task_count

    def do_task(self, ig_media):
        last_max_id = ig_media['next_max_id']

        if "ranked_items" in ig_media:
            key = "ranked_items"
        else:
            key = "items"

        for ig in ig_media[key]:

            if self.task.api.like(ig["pk"]):
                print "*** [" + str(self.task.task_count) + "] Liked a picture!"
                self.task.task_count += 1
            else:
                print "--- Could not send like... trying again"
            time.sleep(self.task.get_time_delay())

        return last_max_id
