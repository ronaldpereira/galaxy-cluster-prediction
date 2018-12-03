import argparse

def parser():
    parser = argparse.ArgumentParser(description='Sloan Digital Sky Survey dataset class prediction using Artificial Neural Networks (ANN).')

    # Required arguments
    parser.add_argument('input_path', type=str, help='Input file path')

    # Optional arguments
    parser.add_argument('-b', '--batch_size', type=int, default=1, help='Training batch size. (Default: 1)')
    parser.add_argument('-e', '--epochs', type=int, default=20, help='Number of training epochs. (Default: 20)')
    parser.add_argument('-l', '--hidden_layers', type=int, default=2, help='Number of hidden layers. (Default: 2)')
    parser.add_argument('-s', '--hidden_layers_size', type=int, default=500, help='Size of hidden layers. (Default: 200)')

    args = parser.parse_args()

    return args
