from sklearn.preprocessing import LabelBinarizer

class DataPreprocessing:
    def __init__(self):
        self.lb = LabelBinarizer()

    def class_encoder(self, class_col):
        class_encoded = self.lb.fit_transform(class_col)

        return class_encoded
