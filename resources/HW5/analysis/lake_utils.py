"""lake_utils.py"""


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_style("darkgrid")


def merge_data():
    """
    I need to be able to export this table so I can	share the .csv
    with my advisor.
    """
    flux = pd.read_csv('~/Dropbox/CSE599/Kuhn/HW5/data/flux.csv')
    chemistry = pd.read_csv('~/Dropbox/CSE599/Kuhn/HW5/data/lakes.csv')

    # Join the two datasets.
    merged_data = pd.concat([chemistry, flux], axis=1)
    merged_data.to_csv('merged_data.csv')
    return merged_data


def plot_CH4(x, y, filename):
    fig = plt.scatter(x, y, alpha=0.5)
    plt.savefig(filename)
    print("Great job using my widget")
