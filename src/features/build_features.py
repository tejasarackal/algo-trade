import numpy as np
from sklearn import preprocessing


def build_features(stock_df):
    x = np.array(stock_df.drop('label', 1))
    preprocessing.scale(x)  # pre-processing to scale the outcomes
    return x


def outcome(stock_df):
    return np.array(stock_df['label'])
