"""
Students have become secret admirers of SEGP. They find the course exciting and the professors amusing. After a superb Mid Semester examination its now time for the results. The TAs have released the marks of students in the form of an array, where arr[i] represents the marks of the ith student.

Since you are a curious kid, you want to find all the marks that are not smaller than those on its right side in the array.

Input Format
The first line of input will contain a single integer n denoting the number of students.
The next line will contain n space separated integers representing the marks of students.
"""
'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
n=int(input())
lst=list(map(int,input().split()))
op_lst=[]
for i in range(n):
    x=False
    for j in range(i,n):
        if lst[i]>=lst[j]:
            x=True
        else:
            x=False
            break
    if x==True:
        op_lst.append(lst[i])
print(" ".join(list(map(str,op_lst))))
        
