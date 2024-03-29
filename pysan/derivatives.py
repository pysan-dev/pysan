# AUTOGENERATED! DO NOT EDIT! File to edit: 22_derivatives.ipynb (unless otherwise specified).

__all__ = ['get_motif', 'get_modal_state']

# Cell
def get_motif(sequences):
    "Computes the motif for a given collection of sequences. A motif is a representative sequence for all sequences in a collection, with blank values (0) being those which are variable within the collection, and fixed values which are not. Motifs are related to the measure of synchrony (see `get_synchrony`) in that synchrony is equal to the number of non-blank elements in the motif."

    shortest_sequence = min([len(s) for s in sequences])

    same_elements = []
    for position in range(shortest_sequence):

        elements_at_this_position = []
        for sequence in sequences:
            elements_at_this_position.append(sequence[position])

        if elements_at_this_position.count(elements_at_this_position[0]) == len(elements_at_this_position):
            same_elements.append(sequences[0][position])
        else:
            same_elements.append(0)

    return same_elements

# Cell
def get_modal_state(sequences):
    "Computes the modal states for each position in a collection of sequences, returning a sequence of tuples containing the modal element and its number of occurances at that position."

    longest_sequence = max([len(s) for s in sequences])

    modal_elements = []
    for position in range(longest_sequence):

        elements_at_this_position = []
        for sequence in sequences:
            try:
                elements_at_this_position.append(sequence[position])
            except:
                continue

        # this line leaves multi-modal position behaviour undefined
        modal_element = max(set(elements_at_this_position), key=elements_at_this_position.count)

        modal_elements.append((modal_element, elements_at_this_position.count(modal_element)))

    return modal_elements