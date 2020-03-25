# Monk and Welcome Problem
"""
Having a good previous year, Monk is back to teach algorithms and data structures. This year he welcomes the learners with a problem which he calls "Welcome Problem". The problem gives you two arrays A and B (each array of size N) and asks to print new array C such that:
 ; 
Now, Monk will proceed further when you solve this one. So, go on and solve it :)
"""
'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
print(' '.join(list(map(str,[A[i]+B[i] for i in range(n)]))))
