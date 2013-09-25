dna_str='AGTCGATGN'

def get_gc(dna):
    dna=dna.replace('N','')    
    gc_count=dna.count('G') + dna.count('C')
    my_gc=gc_count/float(len(dna))
    
    return my_gc

print get_gc(dna_str)
