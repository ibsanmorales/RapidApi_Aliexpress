from dotenv import load_dotenv
load_dotenv()
import os
import http.client
import json
#Class to consume RapiApi - Aliexpress
class AliApi:
    #constructor
    def __init__(self,country):
        #Set main Url and headers 
        self.conn = http.client.HTTPSConnection(os.environ.get("MAGIC_ALIEXPRESS_URL"))
        self.headers = {
            'x-rapidapi-host': os.environ.get("MAGIC_ALIEXPRESS_URL"),
            'x-rapidapi-key': os.environ.get("RAPIDAPI_KEY")
            }
        self.country = country
        self.originCountry ='CN'
    #GET Products Searching
    def getProductsbySearch(self,searchWord, minPrice,maxPrice):
        self.conn.request("GET", f"/api/products/search?name={searchWord}&minSalePrice={minPrice}&shipToCountry={self.country}&sort=NEWEST_DESC&page=1&maxSalePrice={maxPrice}&shipFromCountry={self.originCountry}", 
        headers=self.headers)
        res= self.conn.getresponse()
        data = json.loads(res.read())
        return data
    #GET Product Historic Price
    def getHistoricPricebyProduct(self,productId):
        self.conn.request("GET", f"/api/product/{productId}/historic/prices", 
        headers=self.headers)
        res= self.conn.getresponse()
        data = json.loads(res.read())
        return data
    #GET Product Historic Sales
    def getHistoricSalesbyProducts(self,productId):
        self.conn.request("GET", f"/api/product/{productId}/historic/sales", 
        headers=self.headers)
        res= self.conn.getresponse()
        data = json.loads(res.read())
        return data
    #Product Best Sales
    def getProductsbyBestSales(self,searchByName,minPrice,maxPrice):
        self.conn.request("GET", f"/api/bestSales/products?page=1&priceMax={maxPrice}&priceMin={minPrice}&sort=EVALUATE_RATE_ASC&searchName={searchByName}", 
        headers=self.headers)
        res= self.conn.getresponse()
        data = json.loads(res.read())
        return data

    #GET Product feedbacks
    def getFeedbacksbyProduct(self,productId):
        self.conn.request("GET", f"/api/product/{productId}/feedbacks?page=1", 
        headers=self.headers)
        res= self.conn.getresponse()
        data = json.loads(res.read())
        return data