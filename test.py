#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

import json
import time

from bot.lib.InstagramAPI import InstagramAPI

api = InstagramAPI("", "")
api.login()  # login


def print_to_file(data, name="output.txt"):
    with open(name, "w") as outfile:
        json.dump(api.LastJson, outfile)


tag = "enduro"
counter = 1
like_delay = 15

api.getHashtagFeed(tag)

while counter <= 400:

    media_id = api.LastJson

    if "next_max_id" not in media_id:
        print_to_file(media_id, "no_max_id_data.txt")
        print "Will exit because there is not max_id"
        exit(0)

    last_max_id = media_id['next_max_id']

    if "ranked_items" in media_id:
        key = "ranked_items"
    else:
        key = "items"

    for ig in media_id[key]:

        if api.like(ig["pk"]):
            print "*** [" + str(counter) + "] Liked a picture!"
            counter += 1
        else:
            print "--- Could not send like... trying again"
        time.sleep(like_delay)

    api.getHashtagFeed(tag, maxid=last_max_id)

print "Finished liking IG pics. Total likes sent = " + str(counter)
print "Goodbye"

