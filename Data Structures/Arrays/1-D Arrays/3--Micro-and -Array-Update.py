# Micro and Array Update
"""
Micro purchased an array A having N integer values. After playing it for a while, he got bored of it and decided to update value of its element. In one second he can increase value of each array element by 1. He wants each array element's value to become greater than or equal to K. Please help Micro to find out the minimum amount of time it will take, for him to do so.
"""
'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
t=int(input())
t_lst=[]
lst=[]
for i in range(t):
	a=list(map(int,input().split()))
	b=list(map(int,input().split()))
	t_lst.append([a,b])
for i in t_lst:
    min_i=min(i[1])
    if(i[0][1]>=min_i):
	    print(i[0][1]-min_i)
    else:
        print(0)
