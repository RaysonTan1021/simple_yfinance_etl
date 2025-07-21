import pandas as pd 
import yfinance as yf

### Input Space ### 
ticker = "msft"
csv_path = f"csv_database/{ticker}.csv"
### Input Space ### 

def get_data(ticker, csv_path):
    data = yf.Ticker(ticker)
    df_new = data.history(period="max")

    ### Intuitive try/except block : If read fail, file does not exist, therefore pass to save new df_new as csv 
    try:
        df_old = pd.read_csv(csv_path)
        ### Concatenate all data together, remove duplicated values on "Date", now we're left with unique data 
        df_new = pd.concat([df_old, df_new]).drop_duplicates(subset=['Date']).reset_index(drop=True)
    except:
        print("new data")
        pass
    df_new = df_new
    df_new.to_csv(csv_path)

if __name__ == "__main__":
    get_data(ticker=ticker, csv_path=csv_path)
