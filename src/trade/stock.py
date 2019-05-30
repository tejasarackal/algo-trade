from src.utility.timer import timer
import pandas as pd
import numpy as np
import math


@timer
def label_stock_shift_by_percent(stock_df: pd.DataFrame, label_col, percent=0.01):
    """ labels the stock with value in label column a percent entries before the current entry """
    if label_col in stock_df.columns:
        label_shift = int(math.ceil(percent * len(stock_df)))
        print(label_shift)
        stock_df['label'] = stock_df[label_col].shift(-label_shift)
    return stock_df


@timer
def label_stock_shift_by_number(stock_df: pd.DataFrame, label_col, number=10):
    """ labels the stock with value in label column a number of entries before the current entry """
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
