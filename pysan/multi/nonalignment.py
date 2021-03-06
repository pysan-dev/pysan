# AUTOGENERATED! DO NOT EDIT! File to edit: 24_multi_nonalignment.ipynb (unless otherwise specified).

__all__ = ['get_combinatorial_distance']

# Cell
def get_combinatorial_distance(s1,s2):
    "Computes the combinatorial distance between two sequences. This is defined as 1 minus the number of common subsequences divided by the square root of the product of the number of subsequences in each sequence. See page 149 in Social Sequence Analysis by Benjamin Cornwell for details."

    s1_subs = pysan_core.get_subsequences(s1)
    s2_subs = pysan_core.get_subsequences(s2)

    # parse to strings so that they can be easily compared
    # - haven't tried it without, may be faster...
    s1_subs_strings = [str(s) for s in s1_subs]
    s2_subs_strings = [str(s) for s in s2_subs]

    common_subs = list(set(s1_subs_strings) & set(s2_subs_strings))

    bottom_fraction = math.sqrt(len(s1_subs) * len(s2_subs))
    full_fraction = len(common_subs) / bottom_fraction

    return 1 - full_fraction