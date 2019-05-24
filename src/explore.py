from src.trade.stock import stock_info

from matplotlib import style
from matplotlib import pyplot as plt


if __name__ == '__main__':
    style.use('ggplot')

    tsla_stock = stock_info('TSLA', 2018)

    tsla_ohlc = tsla_stock['Adj Close'].resample('10D').ohlc()
    tsla_volume = tsla_stock['Volume'].resample('10D').sum()

    print(tsla_stock.head())
    ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
    ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=5, colspan=1, sharex=ax1)

    ax1.plot(tsla_stock.index, tsla_stock['Adj Close'])
    ax2.plot(tsla_stock.index, tsla_stock['Volume'])

    plt.show()
