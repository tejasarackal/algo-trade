from pathlib import Path
from src.utility.timer import timer
import datetime as dt
import pandas as pd
import pandas_datareader.data as web
import math
import numpy as np


def clean_data(stock_df):
    stock_df.fillna(-99999, inplace=True)
    return stock_df


@timer
def stock_info(tikr, start_year, end_year):
    """ stock info retrieves the stock price info for the company for a given year """
    if Path(f'data/raw/{tikr}_{start_year}_{end_year}').is_file():
        # if data is stored locally fetch it
        df = pd.read_csv(f'data/raw/{tikr}_{start_year}_{end_year}', parse_dates=True, index_col=0)
    else:
        # retrieve info from web and store it locally
        df = web.DataReader(tikr, 'yahoo', dt.datetime(start_year,1,1), dt.datetime(end_year,12,31))
        df.to_csv(f'data/raw/{tikr}_{start_year}_{end_year}')
    return clean_data(df)


@timer
def label_stock_shift_by_percent(stock_df: pd.DataFrame, label_col, percent=0.01):
    """ labels the stock with value in label column a percent entries before the current entry """
    if label_col in stock_df.columns:
        label_shift = int(math.ceil(percent * len(stock_df)))
        print(label_shift)
        stock_df['label'] = stock_df[label_col].shift(-label_shift)
    # stock_df.dropna(inplace=True)
    return stock_df


@timer
def label_stock_shift_by_number(stock_df: pd.DataFrame, label_col, number=10):
    """ labels the stock with value in label column a percent entries before the current entry """
    if label_col in stock_df.columns:
        label_shift = number
        stock_df['label'] = stock_df[label_col].shift(-label_shift)
    return stock_df


def forecast_stock(stock_df: pd.DataFrame, forecast_outcome):
    stock_df['Forecast'] = np.nan
    forecast_index = 0

    for index, values in stock_df[stock_df['label'].isna()].iterrows():
        stock_df.loc[index, 'Forecast'] = forecast_outcome[forecast_index]
        forecast_index += 1

    return stock_df
