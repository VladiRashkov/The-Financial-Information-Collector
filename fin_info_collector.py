import pandas as pd
import requests
from io import StringIO

def country_info(country):
    url = "https://tradingeconomics.com/matrix"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()  

    
    html_content = StringIO(response.text)

    
    df = pd.read_html(html_content)[0]

    
    market_info = df.loc[df["Country"] == country]
    
    return  "\n".join([f"{market_info[col].name}: {market_info[col].values[0]}" for col in market_info])



print(country_info(input("Country you want to search: ")))