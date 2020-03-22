import requests

class Tesco:
    def __init__(self, key):
        print("Init tesco")
        self.key = key
    
    def get_key(self):
        return self.key
    
    def grocery_search(self, str:query):
        