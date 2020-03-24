import requests
from typing import List

class Tesco:
    def __init__(self, key:str) -> None:
        self.key = key
    
    def grocery_search(self, query:str, offset:int=0, limit:int=10) -> List:
        params:dict = {
            "query": query,
            "offset": offset,
            "limit": limit           
        }
        headers:dict = {
            "Ocp-Apim-Subscription-Key": self.key
        }
        base:str = "https://dev.tescolabs.com/grocery/products/"
        
        r = requests.get(base, params=params, headers=headers)
        
        return r.json()["uk"]["ghs"]["products"]["results"]