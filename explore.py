import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.style as style
import pandas as pd
import pandas_datareader.data as web
from pathlib import Path
from utility.timer import timer


@timer
def stock_info(tikr, year):

    if Path(f'trade-data/{tikr}_{year}').is_file():
        df = pd.read_csv(f'trade-data/{tikr}_{year}', parse_dates=True, index_col=0)
    else:
        df = web.DataReader(tikr, 'yahoo', dt.datetime(year,1,1), dt.datetime(year,12,31))
        df.to_csv(f'trade-data/{tikr}_{year}')

    return df


if __name__ == '__main__':
    style.use('ggplot')

    tsla_stock = stock_info('TSLA', 2018)

    tsla_stock.plot()
    plt.show()
