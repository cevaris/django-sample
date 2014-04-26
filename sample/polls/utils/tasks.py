import time
import json

from celery import task

@task()
def process_vote(payload):
    [poll, choice] = serializers.deserialize('json', data)
    print "Starting Vote"
    # time.sleep(5)
    print "Voted '%s' for poll '%s'" % (choice, poll)
    print "Finished Vote"
    return None