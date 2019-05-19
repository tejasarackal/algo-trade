from pathlib import Path
from utility.timer import timer
import datetime as dt
import pandas as pd
import pandas_datareader.data as web


@timer
def stock_info(tikr, year):

    if Path(f'trade-data/{tikr}_{year}').is_file():
        df = pd.read_csv(f'trade-data/{tikr}_{year}', parse_dates=True, index_col=0)
    else:
        df = web.DataReader(tikr, 'yahoo', dt.datetime(year,1,1), dt.datetime(year,12,31))
        df.to_csv(f'trade-data/{tikr}_{year}')

    return df
