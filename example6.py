reader=open('Pitching.csv', 'r')
line=reader.readline()
line=reader.readline() #skip the header

ip_out=0
count=0

while line !='':
    row = line.split(',')   
    ip_out +=row[12]
    count += 1  
 
reader.close()

print ipout
print count
