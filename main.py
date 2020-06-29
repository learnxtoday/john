#!/home/parth/Desktop/git/loopsync/john/env/bin/python3.8

from config import *
from time import gmtime, strftime
from datetime import datetime
from docopt import docopt


usage = '''

John Titor says hi.
Usage:  main.py --new <tweet>
        main.py --show <num>
        main.py (-h | --help)
        main.py --version

Options:

    -h --help   Show this screen.
    --version   Show Version.

'''



'''

Tweepy Functions

'''


def init():
    global api

    # initialize api
    api = create_api()


def feed(num):
    timeline = api.home_timeline(count=num)
    for tweet in timeline:
        name = tweet.user.name
        name = name.upper()
        text = tweet.text

        print(name + ' said\n' + text + "\n\n")


def main():
    args = docopt(usage, version='Something v1')
    if args['--new']:
        text = args['<tweet>']
        api.update_status(text)

    elif args['--show']:
        num = args['<num>']
        feed(num)


if __name__ == "__main__":
    init()
    main()
