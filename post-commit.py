#!/home/parth/Desktop/git/loopsync/john/env/bin/python3.8

from subprocess import check_output
from random import randint
import tweepy
from os import getenv
from dotenv import load_dotenv
load_dotenv()


CONSUMER_KEY = getenv('CONSUMER_KEY')
CONSUMER_SECRET = getenv('CONSUMER_SECRET')
ACCESS_TOKEN = getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = getenv('ACCESS_TOKEN_SECRET')


FLAG = 1

def create_api():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    global FLAG
    try:
        api.verify_credentials()
        print("Authenticated")
        FLAG = 1
        # print(FLAG)

    except Exception as e:
        print("Error Authenticating")
        FLAG = 0
        # print(FLAG)

    return FLAG, api


# initialize api
FLAG, api = create_api()


if FLAG == 1:
    latestCommitCommand = " git log -1 --pretty='%ar : %an : %s - %h'"
    latestCommitHash = " git log -1 --pretty='%h'"
    commitStatsCommand = "git ls-files | xargs cat | wc -l"
    commitMessageCommand = "git log -1 --pretty=%B"
    basename = "basename `pwd`"

    latestCommit = check_output(['bash', '-c', latestCommitCommand])
    commitID = check_output(['bash', '-c', latestCommitHash])
    commitStats = check_output(['bash', '-c', commitStatsCommand])
    commitMessage = check_output(['bash', '-c', commitMessageCommand])
    base = check_output(['bash', '-c', basename])

    # print("Good job! Latest commit is :" + str(latestCommit))
    commitID = commitID.decode('UTF-8').rstrip("\n")
    commitStats = commitStats.decode('UTF-8')
    base = base.decode('UTF-8').rstrip("\n")


    statusList = ["Commit early, commit often. A tip for version controlling, not for relationships! ",
            "Strive for continuous improvement, instead of perfection.",
            "The biggest room in the world is the room for improvement.",
            "It does not matter how slowly you go as long as you do not stop.",
            "The pursuit of mastery",
            "It always seems impossible until it's done.",
            "With the new commit comes improvement in user experience.",
            "With the new commit comes improvement in developer experience.",
            "With the new commit comes more reliability.",
            "With the new commit comes more security.",
            "With the new commit comes more power, more things you can do.",
            "Be yourself; everyone else is already taken.",
            "Give me six hours to chop down a tree and I will spend the first four sharpening the axe",
            "Live as if you were to die tomorrow. Learn as if you were to live forever.",
            "I have not failed. I've just found 10,000 ways that won't work.",
            "Everything you can imagine is real.",
            "Do what you can, with what you have, where you are.",
            "If we knew what it was we were doing, it would not be called research, would it?"
            "The only true wisdom is in knowing you know nothing.",
            ]

    tweet = '[%s]\n%s\n%s#TLC: %s\n#CommitEveryday #100DaysOfCode #thenerdsuperuser #loopsync' % (commitID, statusList[randint(0, 16)], base, commitStats)

    # print(tweet)
    api.update_status(tweet)

