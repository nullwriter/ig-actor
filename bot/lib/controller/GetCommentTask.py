import time
import re
from FileLogger import FileLogger as FL
import datetime

class GetCommentTask:

    def __init__(self, task, name="extract-comment"):
        self.task = task
        self.name = name
        self.comments = []
        self.log = FL('Extracted Comments {:%Y-%m-%d %H:%M:%S}.txt'.format(datetime.datetime.now()))

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

    def do_task(self, ig_media):
        last_max_id = ig_media['next_max_id']

        if "ranked_items" in ig_media:
            key = "ranked_items"
        else:
            key = "items"

        for ig in ig_media[key]:

            self.task.api.getMediaComments(ig["id"])

            for c in reversed(self.task.api.LastJson['comments']):
                txt = c['text']
                if self.check_string(txt):
                    self.comments.append(txt)
                    print "Comment = " + txt.encode('utf-8', 'ignore').decode('utf-8')
                    self.log.add_to_file(txt=txt)

                    self.task.task_count += 1
                    time.sleep(1)

            time.sleep(self.task.get_time_delay())

        return last_max_id

    """""
    Checks if string doesnt contain special non-english characters, @, or Follow Me.
    """""
    def check_string(self,str):
        pattern = re.compile("^(?!follow|followme)[\s\w\d\?><;,\{\}\[\]\-_\+=!\#\$%^&\*\|\']*$")
        return pattern.match(str)

