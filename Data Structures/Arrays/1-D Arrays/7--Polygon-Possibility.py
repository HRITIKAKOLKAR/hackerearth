#Polygon Possibility
"""
You are given length of n sides, you need to answer whether it is possible to make n sided convex polygon with it.

Input : -

First line contains ,no .of testcases.

For each test case , first line consist of single integer ,second line consist of  spaced integers, size of each side.
"""
'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
def poly_poss(n,n_lst):
    max__n_lst=max(n_lst)
    n_lst.remove(max__n_lst)
    if max__n_lst < sum(n_lst):
        return "Yes"
    else:
        return "No"
T=int(input())
for _ in range(T):
    n=int(input())
    n_lst=list(map(int,input().split()))
    print(poly_poss(n,n_lst))
