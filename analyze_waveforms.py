import os   # library needed to search files in directories
import pandas as pd
import matplotlib.pyplot as plt # library needed to plot waveforms
import numpy as np

# checks .csv files in the data/ folder
input_directory = 'data/'

# fetch all waveforms in the input_directory path and stores them in the waveforms list of objects
waveforms = os.listdir(input_directory)

# make empty lists to store analyzed parameters
maximum_list    = []
baseline_list   = []
noise_list      = []

# loops over all waveforms in the waveforms list
for wf in waveforms:
    print(f'opening file {wf}') # prints waveform name

    # loads the csv file into a pandas dataframe (basically an excel spreadsheet with two columns: Time and Ampl)
    df = pd.read_csv(input_directory + wf, header=4)

    # here I used the function max() to look at the maximum value of the list df['Ampl']
    maximum = max(df['Ampl'])
    maximum_list.append(maximum)    # add the computed maximum to the list of maxima
    print(f'The amplitude of the signal is {maximum} V')

    # get baseline value by checking the average of first 50 points of the waveform
    baseline = sum((df['Ampl'])[:50])/len((df['Ampl'])[:50])
    baseline_list.append(baseline)  # add the computed baseline to the list of baselines
    print(f'The baseline is {baseline} V')

    # get noise value by checking the std of first 50 points of the waveform
    noise = np.std((df['Ampl'])[:50])
    noise_list.append(noise)    # add the computed noise to the list of noises
    print(f'The noise is {noise} V')

    # plot waveform using matplotlib. The first argument of the plot() function is the x axis, the second is the y axis
    plt.plot(df['Time'], df['Ampl'])
    plt.show()

print(maximum_list)
print(baseline_list)
print(noise_list)
