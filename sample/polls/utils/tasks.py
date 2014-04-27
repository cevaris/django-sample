from pprint import pprint
import time
import json

from django.core import serializers

from celery import task

@task(name='process_vote')
def process_vote(payload):
    poll, choice = serializers.deserialize('json', payload)
    print "Starting Vote"
    time.sleep(5)
    pprint("Voted '%s' for poll '%s'" % (choice.object, poll.object))
    print "Finished Vote"
    return None