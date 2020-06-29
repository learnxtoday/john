#!/home/parth/Desktop/git/loopsync/john/env/bin/python3.8

from config import *
from time import gmtime, strftime
from datetime import datetime
from subprocess import check_output
from random import randint

latestCommitCommand = " git log -1 --pretty='%ar : %an : %s - %h'"
latestCommitHash = " git log -1 --pretty='%h'"
commitStatsCommand = "git ls-files | xargs cat | wc -l"
commitMessageCommand = "git log -1 --pretty=%B"


latestCommit = check_output(['bash','-c', latestCommitCommand])
commitID = check_output(['bash','-c', latestCommitHash])
commitStats = check_output(['bash','-c', commitStatsCommand])
commitMessage = check_output(['bash','-c', commitMessageCommand])

# print("Good job! Latest commit is :" + str(latestCommit))
commitID = commitID.decode('UTF-8').rstrip("\n")
commitStats = commitStats.decode('UTF-8')


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


# initialize api
api = create_api()

tweet = '[%s]\n%s\nP2#TLC: %s\n#GitCommitShow #CommitEveryday #100DaysOfCode #thenerdsuperuser #loopsync' % (commitID, statusList[randint(0, 16)] , commitStats)

api.update_status(tweet)

