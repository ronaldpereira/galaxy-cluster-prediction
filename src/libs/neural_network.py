from keras.layers import Activation, Dense, InputLayer
from keras.models import Sequential
from keras.optimizers import SGD
from sklearn.metrics import confusion_matrix, precision_recall_fscore_support
import numpy as np

class NeuralNetwork:
    def __init__(self, input_dim, n_classes, hidden_layer, hidden_size, learning_rate):
        self.model = Sequential()
        self.model.add(InputLayer(input_shape=(input_dim,)))

        for _ in range(hidden_layer):
            self.model.add(Dense(hidden_size))
            self.model.add(Activation('sigmoid' if np.random.randint(2) == 1 else 'tanh'))

        self.model.add(Dense(n_classes))
        self.model.add(Activation('softmax'))

        self.model.compile(loss='categorical_crossentropy', optimizer=SGD(lr=learning_rate), metrics=['accuracy'])

        self.model.summary()

    def train(self, x_train, y_train, batch_size=None, epochs=1):
        self.model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.2)

    def test(self, x_test, y_test, label_binarizer):
        test_loss, test_acc = self.model.evaluate(x_test, y_test)

        y_pred = self.model.predict(x_test)

        y_test_decoded = label_binarizer.inverse_transform(y_test)
        y_pred_decoded = label_binarizer.inverse_transform(y_pred)
        unique_classes = np.unique(y_test_decoded)
        
        test_prec, test_recall, test_fscore, test_support = precision_recall_fscore_support(y_test_decoded, y_pred_decoded, labels=unique_classes)

        conf_matrix = confusion_matrix(y_test_decoded, y_pred_decoded, labels=unique_classes)

        print('-'*30)
        print('Test set statistics')
        print('-'*30)
        print('Global statistics')
        print('-'*30)
        print('Loss: %.4f' %test_loss)
        print('Accuracy: %.4f' %test_acc)
        print('-'*30)
        print('Class specific statistics')
        print('-'*30)

        for uc, prec in zip(unique_classes, test_prec):
            print_metric_for_class('Precision', uc, prec, float)
        print('-'*30)

        for uc, rec in zip(unique_classes, test_recall):
            print_metric_for_class('Recall', uc, rec, float)
        print('-'*30)

        for uc, fsc in zip(unique_classes, test_fscore):
            print_metric_for_class('F-Score', uc, fsc, float)
        print('-'*30)

        for uc, sup in zip(unique_classes, test_support):
            print_metric_for_class('Support', uc, sup, int)

        print('-'*30)
        print('Confusion Matrix')
        print('-'*30)
        
        # Pretty print confusion matrix
        print('tr/pr\t' + '\t'.join(unique_classes))
        for index, uc in enumerate(unique_classes):
            conf_matrix_line = '\t'.join(str(conf_matrix[index]).replace('[', '').replace(']', '').split())
            print(uc + '\t' + conf_matrix_line)

        print('-'*30)

def print_metric_for_class(metric_name, class_name, value, valuetype):
    if valuetype == int:
        print('%s for %s: %d' %(metric_name, class_name, value))
    else:
        print('%s for %s: %.4f' %(metric_name, class_name, value))
