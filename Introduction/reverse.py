#Reverse string
#Input : My name is xyz.
#Output : xyz is name My.
string = "Hello I am happy to be here."
splitted = string.split(" ")
print(splitted)

in_reverse = ""
splitted.reverse()
print(splitted)
for i in range(0, len(splitted)):
  in_reverse = in_reverse + " " + splitted[i]

print(in_reverse)
