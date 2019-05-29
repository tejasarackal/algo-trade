import src.trade.stock as stock
from src.models.train_model import TrainModel
from src.models.predict_model import PredictModel
from matplotlib import style
from matplotlib import pyplot as plt


if __name__ == '__main__':
    style.use('ggplot')

    tsla_stock = stock.stock_info('TSLA', 2015,2018)

    # labeling
    tsla_stock = stock.label_stock_shift_by_number(tsla_stock, label_col='Adj Close', number=10)

    # training data
    linear_model = TrainModel('linear')
    linear_model.train(tsla_stock)

    # predicting data
    forecast_model = PredictModel(linear_model.classifier)
    forecast_model.predict(linear_model.x[-10:])

    tsla_stock = stock.forecast_stock(tsla_stock, forecast_model.get_outcome())

    print(tsla_stock.tail())

