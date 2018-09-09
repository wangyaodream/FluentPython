import warnings

import osconfeed

DB_NAME = 'data/schedule1_db'
CONFERENCE = 'conference.115'

class Record:
    def __init__(self,**kwargs):
        self.__dict__.update(kwargs)

def load_db(db):
    raw_data = osconfeed.load()
    warnings.warn('loading '+ DB_NAME)
    for collection,rec_list in raw_data['Schedule'].items():
        record_type = collection[:-1]