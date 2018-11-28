import argparse

def parser():
    parser = argparse.ArgumentParser(description='Sloan Digital Sky Survey dataset class prediction using Artificial Neural Networks (ANN).')

    # Required arguments
    parser.add_argument('input_path', type=str, help='Input file path')

    args = parser.parse_args()

    return args
