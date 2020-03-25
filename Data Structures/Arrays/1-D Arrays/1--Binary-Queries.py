 #Binary Queries
  """
 Some problems appear hard though they are very easy. Today Aakash is stuck in a range query problem. He has been given an array with only numbers 0 and 1. There are two types of queries -

0 L R : Check whether the number formed from the array elements L to R is even or odd and print EVEN or ODD respectively. Number formation is the binary number from the bits status in the array L to R

1 X : Flip the Xth bit in the array

Indexing is 1 based
"""
'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n_q=list(map(int,input().split()))
lst=list(map(int,input().split()))
queries=[]
for _ in range(n_q[1]):
    queries.append(list(map(int,input().split())))
for query in queries:
    if query[0]==0:
        if lst[query[2]-1]==0:
            print("EVEN")
        else:
            print("ODD")
    if query[0]==1:
        if lst[query[1]-1]==1:
            lst[query[1]-1]=0
        else:
            lst[query[1]-1]=1

