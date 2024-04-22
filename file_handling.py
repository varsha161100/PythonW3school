
file=open('text.txt')

# print(file.read())   # it read all the data in the file

# print(file.read(2))   #it the charater from the file


#_______________read line by____________________

# print(file.readline())   # read only one line from file
# print(file.readline())


#__________________print line by line using readline()_____________________

# line=file.readline()

# while line!="":
#       print(line)
#       line=file.readline()


print(file.readlines()) 
 # showing list 
 #  ['hello miss varsha rawat.\n', 'how are u !!!!!!!!!!\n', 'i hope u are fine!!!!!!!!!!!!!\n', 'gss\n', 'dad\n', 'asdf']


for line in file.readlines():
 print(line)

file.close()