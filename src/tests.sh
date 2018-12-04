#!/bin/bash

printf "Please enter the number of tests repetitions you want to do:\n> "
read REP

# DEFAULTS:
# -b 1
# -e 10
# -r 0.01
# -l 2
# -s 200
# python3 sdss_prediction.py -b 1 -e 10 -r 0.01 -l 2 -s 200 input/sdss.csv

I=1
while [ $I -le $REP ]
do
    printf "Executing iteration %d...\n" "$I"

    # Hidden layer depth
    printf "Executing hidden layer depth changes for iteration %d...\n" "$I"

    mkdir -p output/$I/hidden_layer_depth
    python3 sdss_prediction.py -l 1 input/sdss.csv > output/$I/hidden_layer_depth/output1.txt
    python3 sdss_prediction.py -l 2 input/sdss.csv > output/$I/hidden_layer_depth/output2.txt
    python3 sdss_prediction.py -l 3 input/sdss.csv > output/$I/hidden_layer_depth/output3.txt
    python3 sdss_prediction.py -l 4 input/sdss.csv > output/$I/hidden_layer_depth/output4.txt
    python3 sdss_prediction.py -l 5 input/sdss.csv > output/$I/hidden_layer_depth/output5.txt

    # Hidden layer size
    printf "Executing hidden layer size changes for iteration %d...\n" "$I"

    mkdir -p output/$I/hidden_layer_size
    python3 sdss_prediction.py -s 10 input/sdss.csv > output/$I/hidden_layer_size/output1.txt
    python3 sdss_prediction.py -s 50 input/sdss.csv > output/$I/hidden_layer_size/output2.txt
    python3 sdss_prediction.py -s 200 input/sdss.csv > output/$I/hidden_layer_size/output3.txt
    python3 sdss_prediction.py -s 500 input/sdss.csv > output/$I/hidden_layer_size/output4.txt
    python3 sdss_prediction.py -s 1000 input/sdss.csv > output/$I/hidden_layer_size/output5.txt

    # Learning rate
    printf "Executing learning rate changes for iteration %d...\n" "$I"

    mkdir -p output/$I/learning_rate
    python3 sdss_prediction.py -r 0.001 input/sdss.csv > output/$I/learning_rate/output1.txt
    python3 sdss_prediction.py -r 0.005 input/sdss.csv > output/$I/learning_rate/output2.txt
    python3 sdss_prediction.py -r 0.01 input/sdss.csv > output/$I/learning_rate/output3.txt
    python3 sdss_prediction.py -r 0.05 input/sdss.csv > output/$I/learning_rate/output4.txt
    python3 sdss_prediction.py -r 0.1 input/sdss.csv > output/$I/learning_rate/output5.txt

    # Batch size
    printf "Executing batch size changes for iteration %d...\n" "$I"

    mkdir -p output/$I/batch_size
    python3 sdss_prediction.py -b 1 input/sdss.csv > output/$I/batch_size/output1.txt
    python3 sdss_prediction.py -b 2 input/sdss.csv > output/$I/batch_size/output2.txt
    python3 sdss_prediction.py -b 5 input/sdss.csv > output/$I/batch_size/output3.txt
    python3 sdss_prediction.py -b 100 input/sdss.csv > output/$I/batch_size/output4.txt
    python3 sdss_prediction.py -b 500 input/sdss.csv > output/$I/batch_size/output5.txt

    # Total epochs
    printf "Executing total epochs changes for iteration %d...\n" "$I"

    mkdir -p output/$I/epochs
    python3 sdss_prediction.py -e 1 input/sdss.csv > output/$I/epochs/output1.txt
    python3 sdss_prediction.py -e 2 input/sdss.csv > output/$I/epochs/output2.txt
    python3 sdss_prediction.py -e 10 input/sdss.csv > output/$I/epochs/output3.txt
    python3 sdss_prediction.py -e 20 input/sdss.csv > output/$I/epochs/output4.txt
    python3 sdss_prediction.py -e 50 input/sdss.csv > output/$I/epochs/output5.txt

    (( I++ ))
done

printf "Done executing %d tests repetitions\n" "$REP"
