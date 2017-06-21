import json
import logging
import random

log = logging.getLogger()
log.setLevel(logging.DEBUG)

import sys, os
# get this file's directory independent of where it's run from
here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "vendored"))

# import the shared library, now anything in common/ can be referenced as
# `common.something`
import common
import termcolor


def handler(event, context):
    log.debug("Received event {}".format(json.dumps(event)))
    fact = random.choice(common.all_facts())

    desired_color = event.get('queryStringParameters', {}).get('color')

    response = {}
    if desired_color:
        response['random_fact'] = termcolor.colored(fact, desired_color)
    else:
        response['random_fact'] = fact

    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
