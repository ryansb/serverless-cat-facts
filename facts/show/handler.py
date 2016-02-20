from __future__ import print_function

import json
import random
import logging

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


def handler(event, context):
    log.debug("Received event {}".format(json.dumps(event)))

    with open(os.path.join(here, '../catfacts.json')) as fact_file:
        facts = json.load(fact_file)
        print(facts)
        return {
            "random_fact": random.choice(facts)
        }
