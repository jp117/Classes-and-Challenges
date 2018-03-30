def find_it(seq):
    for x in range (0,len(seq)):
        y = seq.count(seq[x])
        if y%2 != 0:
            return seq[x]