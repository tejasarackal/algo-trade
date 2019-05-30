import numpy as np
from sklearn import preprocessing


def build_features(stock_df, label):
    x = np.array(stock_df.drop(label, 1))
    preprocessing.scale(x)  # pre-processing to scale the outcomes
    return x


def outcome(stock_df, label):
    return np.array(stock_df[label])


def reshape_features_from_list(list_: list):
    features = np.array([[feature] for feature in list_])
    features = features.reshape(len(features), -1)
    return features
