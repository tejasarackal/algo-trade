from src.models.base_model import BaseModel


class PredictModel(BaseModel):

    def __init__(self, classifier):
        super().__init__()
        if hasattr(classifier.__class__, 'predict') and callable(getattr(classifier.__class__, 'predict')):
            self.classifier = classifier
        else:
            raise AttributeError

    def predict(self, forecast_features):
        self.x = forecast_features
        self.y = self.classifier.predict(forecast_features)
