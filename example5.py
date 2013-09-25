reader=open('pg76.txt', 'r')
line=reader.readline()
# some comment
total_length=0
line_count=0
while line !='':
    line_count += 1  
    total_length += len(line)
    line=reader.readline()
reader.close()
 
print "line_count: " + str(line_count) +" total_length:" + str(total_length)



