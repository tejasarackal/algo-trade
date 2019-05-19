from trade.stock import stock_info
import matplotlib.pyplot as plt
import matplotlib.style as style


if __name__ == '__main__':
    style.use('ggplot')

    tsla_stock = stock_info('TSLA', 2018)

    plt.show()
