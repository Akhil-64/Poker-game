#Q1. Given an array, check whether the array is in sorted order with recursion.

def sorted_Array(n):
    if len(n)==0 or len(n)==1:#if n is empty or contains only one element then it returns True
        return True
    return n[0]<=n[1] and sorted_Array(n[1:])#check condition and repeat this condition upto the length of an array
    


print("Enter an the length of an Array")
len1=int(input())
arr=[]
print("Enter Elements :")
for i in range(0,len1):
    element=int(input())
    arr.append(element)

if (sorted_Array(arr))==True:#calling the function
    print("Array is Sorted (ascending order)")
else:
    print("Array is not Sorted")

