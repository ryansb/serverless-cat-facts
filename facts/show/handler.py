import json
import logging
import random

log = logging.getLogger()
log.setLevel(logging.DEBUG)

# this adds the component-level `lib` directory to the Python import path
import sys, os
# get this file's directory independent of where it's run from
here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "../"))
sys.path.append(os.path.join(here, "../vendored"))

# import the shared library, now anything in component/lib/__init__.py can be
# referenced as `lib.something`
import lib
import termcolor


def handler(event, context):
    log.debug("Received event {}".format(json.dumps(event)))
    fact = random.choice(lib.all_facts())

    if event.get('color'):
        return {
            'random_fact': termcolor.colored(fact, event.get('color', 'red'))
        }

    return {
        "random_fact": fact
    }
