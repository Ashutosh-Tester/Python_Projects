#create a for loop to print
#1
#12
#123
#1234
#12345
for i in range(1, 6):
  for j in range(i):
    print(j+1, end="")
  print()