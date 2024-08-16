# import twstock
# stock = twstock.realtime.get(['2603', '6285', '3037'])

from fugle_realtime import HttpClient
from fugle_marketdata import RestClient
exampleList = [3037,2603,6285,1101]

class StockPricing():
    def __init__(self):
        self.token = "MmIwZjllYWUtODdkZC00NDc2LTg4ODgtZWFkMmFkZTE1NzIxIDRlYzA1MDBjLWViNzQtNDIwZi05ZTY1LTlhODBlNjE0YzVjZg=="  
        self.api_client = RestClient(api_key=self.token)
        self.stock = self.api_client.stock

    def getPrice(self, stockList):
        # print(api_client.intraday.volumes(symbolId='2884'))
        if stockList == '':
            stockList = exampleList
        print("ss:",stockList)
        searchResult = []
        for symbolId in  stockList:
            resultObj = {}
            # print("each:",symbolId)
            try:
                quote_data = self.stock.intraday.quote(symbol=symbolId)
                price_data = self.stock.intraday.trades(symbol=symbolId)
                print(quote_data)
                # 股票名稱 & 昨日股價
                stock_name = str(quote_data['name'])
                stock_id = quote_data['symbol']
                referencePrice = str(quote_data['referencePrice']) #參考價
                previousClose = str(quote_data['previousClose']) #收盤價
                changePercent = quote_data['changePercent'] #漲跌幅
                change = quote_data['change'] #漲跌
                date = quote_data['date']
                update_time = quote_data['lastUpdated']
                tradeVolume = quote_data['total']['tradeVolume']
                
                # 即時股價 & 日期 & 即時股價更新時間
                deal = price_data['data'] #交易內容

                resultObj['stock_name'] = stock_name
                resultObj['stock_id'] = stock_id
                resultObj['referencePrice'] = referencePrice
                resultObj['previousClose'] = previousClose
                resultObj['changePercent'] = changePercent
                resultObj['change'] = change
                resultObj['deal'] = deal
                resultObj['date'] = date
                resultObj['update_time'] = update_time
                resultObj['tradeVolume'] = tradeVolume

                # obj = self.api_client.intraday.quote(symbolId=symbolId)
                # obj_price = obj['data']['quote']['trade']['price'] 
                # obj_volume = obj['data']['quote']['trade']['volume']   
                # resultObj["id"] = symbolId
                # resultObj["price"] = obj_price
                # resultObj["volume"] = obj_volume
                searchResult.append(resultObj)
            except Exception as e:
                print("error:",e)
                return e
            # print(searchResult)
        
        return searchResult
        # return obj['data']['quote']['trade']['price']
    def modifiedStockList(self, action, stockId):
        global exampleList
        stockList = exampleList
        print(stockList)
        print(exampleList)
        if action == "remove":
            stockList.remove(int(stockId))
        else:
            stockList.append(int(stockId))
        exampleList = stockList
        return self.getPrice(stockList)

        
if __name__ == "__main__":
    StockPricing().getPrice(['6285','3037'])
