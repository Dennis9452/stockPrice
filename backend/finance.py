# import twstock
# stock = twstock.realtime.get(['2603', '6285', '3037'])

from fugle_realtime import HttpClient

exampleList = [3037,2603,6285,1101]

class StockPricing():
    def __init__(self):
        self.token = "1039572e88751111225a295c62b17b65"  
        self.api_client = HttpClient(api_token=self.token)

    def getPrice(self, stockList):
        # print(api_client.intraday.volumes(symbolId='2884'))
        if stockList == '':
            stockList = exampleList
        print("ss:",stockList)
        searchResult = []
        for symbolId in  stockList:
            resultObj = {}
            print("each:",symbolId)
            try:
                obj = self.api_client.intraday.quote(symbolId=symbolId)
                obj_price = obj['data']['quote']['trade']['price'] 
                obj_volume = obj['data']['quote']['trade']['volume']   
                resultObj["id"] = symbolId
                resultObj["price"] = obj_price
                resultObj["volume"] = obj_volume
                searchResult.append(resultObj)
            except Exception as e:
                print("error:",e)
                return e
            print(searchResult)
        
        return searchResult
        # return obj['data']['quote']['trade']['price']
    def modifiedStockList(self, action, stockId):
        global exampleList
        stockList = exampleList
        if action == "remove":
            stockList.remove(stockId)
        else:
            stockList.append(stockId)
        exampleList = stockList
        return self.getPrice(stockList)

        
if __name__ == "__main__":
    StockPricing().getPrice(['6285','3037'])
