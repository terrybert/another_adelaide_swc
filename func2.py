#Given a string 'filename', write a function which opens that file, iterates over all sequences, and writes a bit of stats about each sequence:

#- print the name of each sequence
#- Count of Ns
#- GC-content
#Print amount of sequences in that file.
#Tips: 
#-  if line.startswith('>') - give the name

def seq_stats(filename):
    reader=open(filename, 'r')
    seq_count=0
    line=reader.readline()        
    while line !='':
        if line.startswith('>'):
            name = line.replace('>','')
            seq_count +=1
        else:
            ncount=line.count('N')
            line.replace('N','')            
            gc_count=line.count('G') + line.count('C')
            my_gc=gc_count/float(len(line))
    print "Sequence: " + name
    print "It has" + ncount +"Ns, " + my_gc + "GC-content"

seq_stats('myfile.txt')
