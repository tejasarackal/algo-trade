from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsClassifier


class BaseModel:
    _models = {'linear': LinearRegression, 'svm': SVR, 'knn': KNeighborsClassifier}

    def __init__(self):
        self.x = None
        self.y = None
        self.classifier = None

    def set_classifier(self, classifier):
        if classifier in self._models:
            self.classifier = self._models[classifier]()
        else:
            raise AttributeError

    def get_features(self):
        return self.x

    def get_outcomes(self):
        return self.y
