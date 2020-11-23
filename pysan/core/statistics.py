# AUTOGENERATED! DO NOT EDIT! File to edit: 16_core_statistics.ipynb (unless otherwise specified).

__all__ = ['is_recurrent', 'get_entropy', 'get_turbulence', 'get_complexity', 'get_routine']

# Cell
def is_recurrent(sequence):
	"Returns true if the given sequence is recurrent (elements can exist more than once), otherwise returns false."	
	element_counts = get_element_counts(sequence)
	
	truths = [count > 1 for element, count in element_counts.items()]
	
	if True in truths:
		return True
	return False

# Cell
def get_entropy(sequence):
	"Computes the normalised [Shannon entropy](https://en.wikipedia.org/wiki/Entropy_(information_theory)) of a given sequence, using the [scipy.stats.entropy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.entropy.html) implementation. Note that this measure is insensitive to transition frequency or event order, so should be used in conjunction with other measures."
	
	alphabet = get_alphabet(sequence)

	entropy = 0
	for state in alphabet:
		proportion_occurances = sequence.count(state) / len(sequence)
		entropy += proportion_occurances * math.log(proportion_occurances)
	
	maximal_occurances = 1 / len(alphabet)
	alphabet_entropy = sum([maximal_occurances * math.log(maximal_occurances) for x in alphabet])
	
	if alphabet_entropy == 0:
		return 0
	
	return -entropy / -alphabet_entropy

# Cell
def get_turbulence(sequence):
	"Computes turbulence for a given sequence, based on [Elzinga & Liefbroer's 2007 definition](https://www.researchgate.net/publication/225402919_De-standardization_of_Family-Life_Trajectories_of_Young_Adults_A_Cross-National_Comparison_Using_Sequence_Analysis) which is also implemented in the [TraMineR](http://traminer.unige.ch/doc/seqST.html) sequence analysis library."

	phi = get_ndistinct_subsequences(sequence)

	#print('phi', phi)

	state_durations = [value for key, value in get_spells(sequence)]

	#print('durations', state_durations)
	#print('mean duration', statistics.mean(state_durations))

	variance_of_state_durations = statistics.variance(state_durations)

	#print('variance', variance_of_state_durations)

	tbar = statistics.mean(state_durations)

	maximum_state_duration_variance = (len(sequence) - 1) * (1 - tbar) ** 2

	#print('smax', maximum_state_duration_variance)

	top_right = maximum_state_duration_variance + 1
	bot_right = variance_of_state_durations + 1

	turbulence = math.log2(phi * (top_right / bot_right))

	#print('turbulence', turbulence)

	return turbulence

# Cell
def get_complexity(sequence):
	"Computes the complexity of a given sequence, based on TraMineR's [seqici](http://traminer.unige.ch/doc/seqici.html) method."
	
	alphabet = get_alphabet(sequence)

	pre_log = 1 / len(alphabet)
	hmax = -math.log(pre_log)
	#print('hmax', hmax)
	if hmax == 0:
		return 0 # all identical elements, no complexity

	hs = get_entropy(sequence)
	#print('hs', hs)

	qs = get_ntransitions(sequence)
	#print('qs', qs)

	qmax = len(sequence) - 1
	#print('qmax', qmax)

	norm_transitions = qs / qmax
	norm_entropy = hs / hmax

	#print('nt', norm_transitions)
	#print('ne', norm_entropy)

	complexity = math.sqrt(norm_transitions * norm_entropy)

	#print('complexity', complexity)
	return complexity

# Cell
def get_routine(sequence, duration):
	"Computes a normalised measure of routine within a sequence for a given duration within that sequence. E.g. with a sequence where each element is one day, calling get_routine() with a duration of 7 would look at weekly routines. Note that this routine measure is identical to the multisequence measure of synchrony, but applied within-sequence in duration length chunks."
	
	if len(sequence) % duration != 0:
		raise Exception('sequence not divisible by interval, check data input')
	
	num_cycles = int(len(sequence) / duration)
	cycles = [sequence[n * duration:n * duration + duration] for n in range(num_cycles)]
	
	return pysan_ms.get_synchrony(cycles)