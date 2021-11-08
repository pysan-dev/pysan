# AUTOGENERATED! DO NOT EDIT! File to edit: 21_attributes.ipynb (unless otherwise specified).

__all__ = ['are_recurrent', 'get_summary_statistic', 'get_routine_scores', 'get_synchrony', 'get_sequence_frequencies']

# Cell
from .statistics import is_recurrent
def are_recurrent(sequences):
    "Returns true if any of the sequences in a given collection are recurrant, false otherwise."

    for sequence in sequences:
        if is_recurrent(sequence):
            return True

    return False

# Cell
def get_summary_statistic(sequences, function):
    "Computes a summary statistic (e.g. entropy, complexity, or turbulence) for each sequence in a collection, returning the results as a list."
    return [function(s) for s in sequences]

# Cell
from .statistics import get_routine
def get_routine_scores(sequences, duration):
    "Returns a list containing the routine scores for each sequence in a collection using :meth:`get_routine() <pysan.core.get_routine>`."
    return [get_routine(s, duration) for s in sequences]

# Cell
def get_synchrony(sequences):
    "Computes the normalised synchrony between a two or more sequences. Synchrony here refers to positions with identical elements, e.g. two identical sequences have a synchrony of 1, two completely different sequences have a synchrony of 0. The value is normalised by dividing by the number of positions compared. This computation is defined in Cornwell's 2015 book on social sequence analysis, page 230."

    shortest_sequence = min([len(s) for s in sequences])

    same_elements = []
    for position in range(shortest_sequence):

        elements_at_this_position = []
        for sequence in sequences:
            elements_at_this_position.append(sequence[position])

        same_elements.append(elements_at_this_position.count(elements_at_this_position[0]) == len(elements_at_this_position))

    return same_elements.count(True) / shortest_sequence

# Cell
def get_sequence_frequencies(sequences):
    "Computes the frequencies of different sequences in a collection, returning a dictionary of their string representations and counts."

    # converting to strings makes comparison easy
    sequences_as_strings = [str(s) for s in sequences]

    sequence_frequencies = {}
    for sequence in set(sequences_as_strings):
        sequence_frequencies[sequence] = sequences_as_strings.count(sequence)

    sequence_frequencies = {k: v for k, v in sorted(sequence_frequencies.items(), key=lambda item: item[1], reverse=True)}

    return sequence_frequencies