import pandas as pd
from sklearn.model_selection import train_test_split

import libs.arg_parse_config as APC
import libs.data_preprocessing as DP
import libs.neural_network as NN

import warnings
warnings.filterwarnings('ignore')

args = APC.parser()

sdss = pd.read_csv(args.input_path)

data_prep = DP.DataPreprocessing()

# Uncomment the line below to balance QSO class
# sdss = data_prep.balance_class(sdss, 'QSO', 6)

encoded_classes = data_prep.class_encoder(sdss['class'])

x_train, x_test, y_train, y_test = train_test_split(sdss.drop('class', axis=1).values, encoded_classes, train_size=0.666)

nn = NN.NeuralNetwork(x_train.shape[1], y_train.shape[1], args.hidden_layers, args.hidden_layers_size, args.learning_rate)

nn.train(x_train, y_train, batch_size=args.batch_size, epochs=args.epochs)

nn.test(x_test, y_test, data_prep.lb)
