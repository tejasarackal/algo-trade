from src.models.train_model import TrainModel
from src.models.predict_model import PredictModel
from src.features.build_features import reshape_features_from_list
import src.data.make_dataset as dataset


if __name__ == '__main__':

    cancer_df = dataset.cancer_info()

    # Train the model for k nearest neighbors
    knn_model = TrainModel('knn')
    knn_model.train(cancer_df, label='class', test_percent=0.2)

    # Set the classifier in your prediction model
    predict_model = PredictModel(knn_model.classifier)

    # Build & reshape the features you want to predict/forecast
    forecast_features = reshape_features_from_list([[5,10,10,10,4,10,5,6,3],[1,1,1,1,2,1,1,1,1]])
    print(f'\nForecasting features i/p: \n {forecast_features} \n')

    # Predict & print the outcome class for the forecast features
    predict_model.predict(forecast_features)
    print(f'Prediction o/p: {predict_model.get_outcomes()}')
