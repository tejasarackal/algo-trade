from matplotlib import style
from matplotlib import pyplot as plt
from contextlib import contextmanager


@contextmanager
def display_context(style_):
    style.use(style_)
    try:
        yield
    finally:
        plt.show()


def display_stock(stock_df, cols, xlabel, ylabel):
    with display_context('ggplot'):
        for col in cols:
            stock_df[col].plot()

        plt.legend(loc=4)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
