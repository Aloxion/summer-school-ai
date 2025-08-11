import pyedflib
# https://pyedflib.readthedocs.io/en/latest/ref/edfreader.html
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Need to find out stationary with test
# need to plot for autocorrelation

def read_eeg_data(file_path, length=0):
    with pyedflib.EdfReader(file_path) as f:
        n = f.signals_in_file
        length = n;
        signal_data = [f.readSignal(i) for i in range(n)]
        metadata = {
            'signal_labels': f.getSignalLabels(),
            'sample_rate': f.getSampleFrequency(0),
            'duration': f.file_duration
        }
    return signal_data, metadata, length



path = "seizure_eeg_data/01.edf"
signal_data, metadata, length = read_eeg_data(path)
str_to_print = ""
for label, i in enumerate(metadata['signal_labels']):
    str_to_print += f"Label {label}: {i}\n"
str_to_print += f"Sample Rate: {metadata['sample_rate']} Hz\n"
str_to_print += f"Duration: {metadata['duration']} seconds\n"
for i in range(length):
    str_to_print += f"Sample {i}: {signal_data[0][i]}\n"  # Print first signal's sample value
# print(str_to_print)

# use pd.plotting.autocorrelation_plot for the signals

print("Plotting Autocorrelation for the first signal...")

# Creating Autocorrelation plot
x = pd.plotting.autocorrelation_plot(signal_data[0])

# plotting the Curve
x.plot()

pd.tseries.plotting.pylab.show()
