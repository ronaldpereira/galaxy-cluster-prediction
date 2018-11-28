from keras.layers import Activation, Dense, InputLayer
from keras.models import Sequential
from keras.optimizers import Adam

class NeuralNetwork:
    def __init__(self, input_dim, n_classes):
        self.model = Sequential()
        self.model.add(InputLayer(input_shape=(input_dim,)))
        self.model.add(Dense(input_dim**2))
        self.model.add(Activation('relu'))
        self.model.add(Dense(input_dim*100))
        self.model.add(Activation('sigmoid'))
        self.model.add(Dense(n_classes))
        self.model.add(Activation('softmax'))

        self.model.compile(loss='categorical_crossentropy', optimizer=Adam(lr=0.001), metrics=['accuracy'])

        self.model.summary()

    def train(self, x_train, y_train, batch_size=None, epochs=1):
        self.model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.2)

    def test(self, x_test, y_test):
        print(self.model.evaluate(x_test, y_test))
