from pathlib import Path
from src.utility.timer import timer
from src.utility.data_cleaning import fill_missing_data
import pandas as pd
import datetime as dt
import pandas_datareader as web

BASE_DIR = Path(__file__).resolve().parent.parent.parent
RAW_DATA_DIR = BASE_DIR.joinpath('data/raw')


@timer
def stock_info(tikr, start_year, end_year):
    """ stock info retrieves the stock price info for the company for a given year """
    if Path(f'{RAW_DATA_DIR}/{tikr}_{start_year}_{end_year}.db').is_file():
        # if data is stored locally fetch it
        df = pd.read_csv(f'{RAW_DATA_DIR}/{tikr}_{start_year}_{end_year}.db', parse_dates=True, index_col=0)
    else:
        # retrieve info from web and store it locally
        df = web.DataReader(tikr, 'yahoo', dt.datetime(start_year,1,1), dt.datetime(end_year,12,31))
        df.to_csv(f'{RAW_DATA_DIR}/{tikr}_{start_year}_{end_year}.db')
    return fill_missing_data(df)


def cancer_info():
    filename = 'breast-cancer-wisconsin.data'

    if RAW_DATA_DIR.joinpath(f'{filename}').is_file():
        df = pd.read_csv(f'{RAW_DATA_DIR}/{filename}')
        df.replace('?', -99999, inplace=True)

        df.drop(['id'], 1, inplace=True)
        return df
    else:
        raise FileNotFoundError


if __name__ == '__main__':
    cancer_info()
