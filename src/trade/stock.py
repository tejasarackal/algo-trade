from pathlib import Path
from src.utility.timer import timer
import datetime as dt
import pandas as pd
import pandas_datareader.data as web


@timer
def stock_info(tikr, year):
    """ stock info retrieves the stock price info for the company for a given year """
    if Path(f'data/raw/{tikr}_{year}').is_file():
        # if data is stored locally fetch it
        df = pd.read_csv(f'data/raw/{tikr}_{year}', parse_dates=True, index_col=0)
    else:
        # retrieve info from web and store it locally
        df = web.DataReader(tikr, 'yahoo', dt.datetime(year,1,1), dt.datetime(year,12,31))
        df.to_csv(f'data/raw/{tikr}_{year}')
    return df
