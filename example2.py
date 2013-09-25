#given a string (a sentence), find out how many
#unique letters A-Z it contains - capital and
#lower case shouldn't be double-counted
#'AaAa'
#input: some string
#input_string = 'some string here'
#print (the number of unique letters in the string)

input_string = 'Another some string here'
newstr=input_string.lower()
my_set=set(newstr)

l=len(my_set)

print l
