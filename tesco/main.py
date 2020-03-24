import requests
from typing import List

class Tesco:
    def __init__(self, key:str) -> None:
        print("Init tesco")
        self.key = key
    
    def grocery_search(self, query:str, offset:int=0, limit:int=10) -> List:
        params = {
            "query": query,
            "offset": offset,
            "limit": limit           
        }
        headers = {
            "Ocp-Apim-Subscription-Key": self.key
        }
        base = "https://dev.tescolabs.com/grocery/products/"
        
        r = requests.get(base, params=params, headers=headers)
        
        for item in r.json()["uk"]["ghs"]["products"]["results"]:
            yield item["name"]