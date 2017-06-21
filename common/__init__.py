# shared logic goes here
import json
import os

here = os.path.dirname(os.path.realpath(__file__))

def all_facts():
    with open(os.path.join(here, '../catfacts.json')) as fact_file:
        facts = json.load(fact_file)
        return facts
