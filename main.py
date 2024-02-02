import requests
import pandas as pd
from datetime import datetime
import time

def timenow():
    return datetime.strftime(datetime.now(), "%m-%d-%Y %H:%M:%S")

def scraper1(url):
    while True:
        
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse JSON data
            outages_data = response.json()

            # DataFrame
            df = pd.DataFrame(outages_data)
            
            # Dataframe to CSV
            if not df.empty:
                df.to_csv("info.csv", index=False)
                print(f"Data saved to info.csv at {timenow()} successfully.")
            else:
                print(f"No data to save at {timenow()}.")

            # 15 mins
            time.sleep(900)
        else:
            print(f"Failed to fetch data from the URL at {timenow()}.") #if no data

if __name__ == "__main__":
    url = "https://outage.canoocheeemc.com:8889/data/outages.json"
    scraper1(url)
