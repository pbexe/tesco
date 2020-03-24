import requests
from typing import List

class Tesco:
    """The Tesco wrapper object
    """
    
    def __init__(self, key:str) -> None:
        """init
        
        Args:
            key (str): The API key
        """
        
        self.key = key
    
    def grocery_search(self, query:str, offset:int=0, limit:int=10) -> List:
        """Searches grocery items stocked by Tescolabs
        
        ```
        Args:
            query (str): The search query
            offset (int, optional): The offset used for pagination. Defaults to 0.
            limit (int, optional): The number of results to return. Defaults to 10.
        
        Returns:
            List: List of products
        ```
        """
        
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
    
    def product_data(self, gtin:str="", tpnb:str="", tpnc:str="", catid:str="") -> List:
        """Gets information about a product
        
        ```
        Args:
            gtin (str, optional): The gtin of the product. Defaults to "".
            tpnb (str, optional): The tpnb of the product. Defaults to "".
            tpnc (str, optional): The tpnc of the product. Defaults to "".
            catid (str, optional): The catid of the product. Defaults to "".
        
        Returns:
            List: The information about the product
        ```
        """
        
        params:dict = {
            "gtin": gtin,
            "tpnb": tpnb,
            "tpnc": tpnc,          
            "catid": catid
        }
        cleaned_params:dict = {k: v for k, v in params.items() if v is not ""}
        headers:dict = {
            "Ocp-Apim-Subscription-Key": self.key
        }
        base:str = "https://dev.tescolabs.com/product/"
        
        r = requests.get(base, params=cleaned_params, headers=headers)
        
        return r.json()["products"]