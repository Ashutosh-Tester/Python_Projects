
"""
create a for loop to print
1
12
123
1234
12345

"""


rows = 5
def print_num_pattern():
    # for loop for rows
    for i in range(1,rows+1):
        # for loop for colums
        for j in range(1,i+1):
            # print results
            print(j,end=" ")
        print(" ")
    
def main():
    print_num_pattern()

main()