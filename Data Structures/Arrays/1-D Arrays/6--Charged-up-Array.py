#Charged Up Array
"""
You are given with an array  of size .An element  is said to be charged if its value() is greater than or equal to .  is the total number of subsets of array , that consist of element . 
Total charge value of the array is defined as summation of all charged elements present in the array mod .
Your task is to output the total charge value of the given array .

INPUT FORMAT:

The first line of input contains number of test cases .
The first line of each test case consists of , the size of the array.
Next line contains  space-separated integers corresponding to each element .
"""
def solve (A,N,mod):
    # Write your code here mod=int(pow(10,9)+7)
    sum=0
    Ki=int(pow(2,N)//2)
    for Ai in A:
        if Ai>=Ki:
            sum+=Ai
    return sum%mod

T = int(input())
mod=int(pow(10,9)+7)
for _ in range(T):
    N = int(input())
    A = map(int, input().split())

    out_ = solve(A,N,mod)
    print (out_)
