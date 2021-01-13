# AUTOGENERATED! DO NOT EDIT! File to edit: 20_multi_overview.ipynb (unless otherwise specified).

__all__ = ['plot_sequences']

# Cell
import matplotlib.pyplot as plt
import numpy as np
from ..core.elements import get_alphabet
def plot_sequences(sequences, gap=True):
    "Creates a scatter style sequence plot for a collection of sequences."
    max_sequence_length = max([len(s) for s in sequences])
    plt.figure(figsize=[max_sequence_length*0.3,0.3 * len(sequences)])

    for y,sequence in enumerate(sequences):
        np_sequence = np.array(sequence)
        alphabet_len = len(get_alphabet(sequence))

        plt.gca().set_prop_cycle(None)
        unique_values = get_alphabet(sequence)
        for i, value in enumerate(unique_values):

            if gap:
                points = np.where(np_sequence == value, y + 1, np.nan)
                plt.scatter(x=range(len(np_sequence)), y=points, marker='s', label=value, s=100)
            else:
                points = np.where(np_sequence == value, 1, np.nan)
                plt.bar(range(len(points)), points, bottom=[y for x in range(len(points))], width=1, align='edge', label=i)

    if gap:
        plt.ylim(0.4, len(sequences) + 0.6)
        plt.xlim(-0.6, max_sequence_length - 0.4)
    else:
        plt.ylim(0,len(sequences))
        plt.xlim(0,max_sequence_length)

    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys(), bbox_to_anchor=(1.0, 1.1), loc='upper left')
    plt.tick_params(
        axis='y',
        which='both',
        left=False,
        labelleft=False)

    return plt