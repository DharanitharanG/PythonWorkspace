import pandas as pd
import matplotlib.pyplot as plt
import numpy

pd.set_option('display.max_columns', 5)


def get_data_frame(input_path, skip_lines, data_columns):
    df = pd.read_csv(input_path, skiprows=skip_lines)
    df.columns = data_columns
    return df


def plot_data_frame(data_frame, title, x_label, y_label):
    data_frame.plot(figsize=(20, 40), linewidth=1, fontsize=10)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    return plt
