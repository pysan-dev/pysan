# AUTOGENERATED! DO NOT EDIT! File to edit: 11_core_elements.ipynb (unless otherwise specified).

__all__ = ['get_alphabet', 'get_element_counts', 'get_first_positions', 'get_element_frequency']

# Cell
def get_alphabet(sequence):
	"Computes the alphabet of a given sequence (set of its unique elements)."
	return set(sequence)

# Cell
def get_element_counts(sequence):
	"Counts the number of occurances for each element in a sequence, returning a dictionary containing the elements as keys and their counts as values."
	alphabet = get_alphabet(sequence)
	
	counts = {}
	for element in alphabet:
		counts[element] = sequence.count(element)
		
	return counts

# Cell
def get_first_positions(sequence):
	"Reports the first occurance of each element in the sequence in a dictionary, with each element as keys, and their first position as values."
	unique_elements = list(set(sequence))

	first_positions = {}
	for element in unique_elements:
		first_positions[element] = sequence.index(element)
		
	return first_positions

# Cell
def get_element_frequency(sequence):
	"Computes the relative frequency (aka prevalence or unconditional probability) of each element in a sequence, returning a dictionary where each key is an element and each value is that elements relative frequency."
	alphabet = get_alphabet(sequence)
	
	prevalences = {}
	for element in alphabet:
		prevalences[element] = sequence.count(element) / len(sequence)
		
	return prevalences