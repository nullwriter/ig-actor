#!/usr/bin/env python

import sys

from lib.controller.Main import Main


def get_version():
    return "0.0.2"


def main(argv):
    print "IG-Bot v"+get_version()
    print "Close this window o press CTRL + C if you need to force close the bot."
    print ""
    config_starter(argv)


def config_starter(argv):
    chosen = False

    while not chosen:
        print ""
        print "Tasks available:"
        print "1. Like"
        print "2. Comment"
        print "3. Extract Comments (to file)"
        print ""
        input = raw_input("Choose task (number): ")

        try:
            val = int(input)
            if val == 1 or val == 2 or val == 3:
                chosen = True
                break
        except ValueError:
            print("That's not a number!")

    Main(get_cmd(val))


def get_cmd(num):
    if num == 1:
        return "like"
    if num == 2:
        return "comment"
    if num == 3:
        return "extract-comment"

if __name__ == "__main__":
    main(sys.argv)
