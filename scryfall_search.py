import sys
import json
import ijson
import time
# import requests

class CardBulk:
    def __init__ (self, bulk_file):
        self.bulk_file = bulk_file
        self.db = {}
        self.load_bulk()

    def search_mtgoid(self, mtgo_id):    
        card = self.db.get(int(mtgo_id))
        return card

    def load_bulk(self):
        with open(self.bulk_file, 'rb') as f:
            cards = ijson.items(f, 'item')
            for card in cards:
                mtgo_id = card.get('mtgo_id')
                if mtgo_id is not None:
                    self.db[mtgo_id] = card
