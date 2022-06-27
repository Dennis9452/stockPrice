import requests
from bs4 import BeautifulSoup
import pandas as pd

class NBAstats:
   
    def getStats():
        # year=input("Which NBA season are you interested in?: ")
        # count=input("how many player you want to know?")
       
        player_list = ['Trae Young','Nikola Jokić','Luka Dončić']
        print(player_list)
        # player=input("For which player do you want to get stats?: ")
        
        url = 'https://www.basketball-reference.com/leagues/NBA_2022_per_game.html'
    
        r = requests.get(url)
        r_html = r.text
        soup = BeautifulSoup(r_html,'html.parser')
        table=soup.find_all(class_="full_table")

         # """ Extracting List of column names"""
        head=soup.find(class_="thead")
        column_names_raw=[head.text for item in head][0]
        column_names_polished=column_names_raw.replace("\n",",").split(",")[2:-1]
        print(column_names_polished)

        players=[]
        for i in range(len(table)):
            player_=[]
            
            for td in table[i].find_all("td"):
                player_.append(td.text)

            players.append(player_)
            df = pd.DataFrame(players, columns=column_names_polished)
            # df = df.set_index("Player",drop=False)   
        # print(df)
        return df


    def getTable( playerList, data ):
        print("playerList:",playerList)
        df = data.set_index("Player")   
        if(not playerList): 
            playerList = []
        result = df.loc[playerList,["G","TRB","AST","STL","BLK","TOV","PTS"]]  
        print(type(result))
        return result  
    def getPlayer( data ):
        alphabeticList = {
                            "ć" : "c",
                            "č" : "c",
                            "á" : "a",
                            "š" : "s",
                            "ý" : "y",
                            "é" : "e",
                            "ó" : "o"
        }
        print(data)
        all_player = data["Player"]
        # for td in data["Pos"]:
        #     all_player.append(td)
       
        return all_player

        
if __name__ == "__main__":
    NBAstats.getPlayer( NBAstats.getStats())
    NBAstats.getTable( ['Trae Young','Nikola Jokić','Luka Dončić'],NBAstats.getStats())