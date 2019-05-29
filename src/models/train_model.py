from sklearn.model_selection import train_test_split
from src.features.build_features import build_features
from src.features.build_features import outcome
from src.models.base_model import BaseModel


class TrainModel(BaseModel):

    def __init__(self, classifier):
        super().__init__()
        self.set_classifier(classifier)

    def train(self, stock_df, test_percent=0.2):

        # data cleansing
        clean_stock_df = stock_df.dropna(inplace=False)

        # deriving features and outcome from the data to be trained upon
        self.x = build_features(clean_stock_df)
        self.y = outcome(clean_stock_df)

        # split data into training and test data set
        x_train, x_test, y_train, y_test = train_test_split(self.x, self.y, test_size=test_percent)

        # choosing the classifier and fit the parameters for the training dataset
        self.classifier.fit(x_train, y_train)

        # now we calculate the accuracy of our linear model
        print(self.classifier.score(x_test, y_test))
