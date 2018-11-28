import pandas as pd
from sklearn.model_selection import train_test_split

import libs.neural_network as NN
import libs.arg_parse_config as APC
import libs.data_preprocessing as DP

import warnings
warnings.filterwarnings('ignore')

args = APC.parser()

sdss = pd.read_csv(args.input_path)

data_prep = DP.DataPreprocessing()

encoded_classes = data_prep.class_encoder(sdss['class'])

x_train, x_test, y_train, y_test = train_test_split(sdss.drop('class', axis=1).values, encoded_classes, train_size=0.8)

nn = NN.NeuralNetwork(x_train.shape[1], y_train.shape[1])

nn.train(x_train, y_train, round(x_train.shape[0]/4), epochs=40)

nn.test(x_test, y_test)
