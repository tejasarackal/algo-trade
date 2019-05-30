import src.data.make_dataset as dataset
import src.trade.stock as stock
from src.models.train_model import TrainModel
from src.models.predict_model import PredictModel
import src.visualization.vizualize as visual


if __name__ == '__main__':

    tsla_stock = dataset.stock_info('TSLA', 2015,2018)

    # labeling
    tsla_stock = stock.label_stock_shift_by_number(tsla_stock, label_col='Adj Close', number=10)

    # training data
    linear_model = TrainModel('linear')
    linear_model.train(tsla_stock, label='label')

    # predicting data
    forecast_model = PredictModel(linear_model.classifier)
    forecast_model.predict(linear_model.x[-10:])

    tsla_stock = stock.forecast_stock(tsla_stock, forecast_model.get_outcomes())
    visual.display_stock(tsla_stock, cols=['Adj Close', 'Forecast'], xlabel='Date', ylabel='Price')