import pandas as pd
from sklearn.preprocessing import LabelBinarizer

class DataPreprocessing:
    def __init__(self):
        self.lb = LabelBinarizer()

    def class_encoder(self, class_col):
        class_encoded = self.lb.fit_transform(class_col)

        return class_encoded

    def balance_class(self, dataframe, class_to_balance, multiplier):
        class_df = dataframe.loc[dataframe['class'] == class_to_balance].reset_index().copy()

        concat_array = [dataframe]

        for _ in range(multiplier-1):
            concat_array.append(class_df)

        dataframe = pd.concat(concat_array, ignore_index=True)

        return dataframe
