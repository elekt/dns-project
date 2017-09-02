from util import get_random_base, get_base_pair, make_m_rns, get_aminoacids

sense = []
start_codon = [('A', get_base_pair('A')), ('T', get_base_pair('T')), ('G', get_base_pair('G'))]
stop_codon = [('A', get_base_pair('A')), ('T', get_base_pair('T')), ('T', get_base_pair('T'))]
sense.extend(start_codon)
for i in range(0, 21):
    base = get_random_base()
    pair = get_base_pair(base)
    sense.append((base, pair))
sense.extend(stop_codon)

m_rns = make_m_rns(sense)
print("mRNS: {}".format(m_rns))

amino_acids = get_aminoacids(m_rns)
print("amino acids: {}".format(amino_acids))
