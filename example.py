import sys

#1. get the list of arguments
my_list = sys.argv[1:]

#2. sort them
my_list.sort()

#3. join all of the words except the last one with a comma
sentence = ', '.join(my_list[0:-1])

#[4. capitalize the first letter]
#5. append the word "and" and the final word, and a period

sentence += ', and ' + my_list[-1] + '.'
#6. print the result
print sentence.capitalize()





