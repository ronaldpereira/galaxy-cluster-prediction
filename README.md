# Sloan Digital Sky Survey Class Prediction

Sloan Digital Sky Survey dataset class prediction using MLP (Multi-Layer Perceptron) Artificial Neural Networks (ANN).

## Usage

```text
usage: sdss_prediction.py [-h] [-b BATCH_SIZE] [-e EPOCHS] [-r LEARNING_RATE]
                          [-l HIDDEN_LAYERS] [-s HIDDEN_LAYERS_SIZE]
                          input_path

Sloan Digital Sky Survey dataset class prediction using MLP (Multi-Layer Perceptron) Artificial Neural
Networks (ANN).

positional arguments:
  input_path            Input file path

optional arguments:
  -h, --help            show this help message and exit
  -b BATCH_SIZE, --batch_size BATCH_SIZE
                        Training batch size. (Default: 1)
  -e EPOCHS, --epochs EPOCHS
                        Number of training epochs. (Default: 10)
  -r LEARNING_RATE, --learning_rate LEARNING_RATE
                        Stochastic Gradient Descent optimizer Learning Rate.
                        (Default: 0.01)
  -l HIDDEN_LAYERS, --hidden_layers HIDDEN_LAYERS
                        Number of hidden layers. (Default: 2)
  -s HIDDEN_LAYERS_SIZE, --hidden_layers_size HIDDEN_LAYERS_SIZE
                        Size of hidden layers. (Default: 200)
```
