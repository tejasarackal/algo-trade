

def fill_missing_data(df):
    df.fillna(-99999, inplace=True)
    return df
